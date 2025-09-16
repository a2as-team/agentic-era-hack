ArgoCD + GitHub Actions: A Complete GitOps CI/CD Workflow for Kubernetes Applications
=====================================================================================

[![Mehmet kanus](https://miro.medium.com/v2/resize:fill:64:64/1*mY4atEXZEL4C63jWxjpdZg.jpeg)](https://medium.com/@mehmetkanus17?source=post_page---byline--ed2f91d37641---------------------------------------)

[Mehmet kanus](https://medium.com/@mehmetkanus17?source=post_page---byline--ed2f91d37641---------------------------------------)

5 min read

·

Jun 30, 2025

[nameless link](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fed2f91d37641&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40mehmetkanus17%2Fargocd-github-actions-a-complete-gitops-ci-cd-workflow-for-kubernetes-applications-ed2f91d37641&user=Mehmet+kanus&userId=8f06d8dffb1f&source=---header_actions--ed2f91d37641---------------------clap_footer------------------)

--

1

[nameless link](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fed2f91d37641&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40mehmetkanus17%2Fargocd-github-actions-a-complete-gitops-ci-cd-workflow-for-kubernetes-applications-ed2f91d37641&source=---header_actions--ed2f91d37641---------------------bookmark_footer------------------)

Listen

Share

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GgIeRA40tqhLPUSpJ1kMzw.png)

In this article, we’ll walk through a real-world GitOps workflow using ArgoCD, GitHub Actions, and Kubernetes. The goal is to automate the deployment pipeline such that:

*   Your application is built with GitHub Actions.
*   Docker images are pushed to GitHub Container Registry (GHCR).
*   ArgoCD detects the updated image tag in your GitOps repository and syncs the Kubernetes manifests accordingly.

This fully automated pipeline ensures consistency, auditability, and speed — all key benefits of modern DevOps practices.

### **Architecture Overview**

1.  CI Pipeline with GitHub Actions
    — Build the application.
    — Tag and push the Docker image to GHCR.
    — Update the image tag in the GitOps repository.
2.  GitOps Repository
    — Contains Kubernetes manifests managed by ArgoCD.
    — ArgoCD syncs changes to kubernetes automatically or manually based on configuration.
3.  ArgoCD
    — Monitors the GitOps repo.
    — Reconciles the desired state (Git) with the live state (Kubernetes).

### **Prerequisites**

-Kubernetes cluster configured and running
- ArgoCD installed on the kubernetes cluster
- A GitHub repository for your application code (CI repo)
- A separate GitHub repository for your Kubernetes manifests (GitOps repo)
- GitHub Container Registry enabled
- kubectl and ArgoCD CLI configured locally

**First, clone the following repositories to your own GitHub account and set them as private:**

*   [argocd-app](https://github.com/mehmetkanus17/argocd-app.git)
*   [argocd-deploy](https://github.com/mehmetkanus17/argocd-deploy.git)

> These repositories contain the application source code and the GitOps deployment manifests respectively.

### Step 1 — Install ArgoCD on Your Kubernetes Cluster Using Helm

To begin, we’ll deploy **ArgoCD** on our existing Kubernetes cluster using the official **Helm chart**. This will set up the GitOps controller that continuously reconciles the state between your Git repository and the cluster.

You can install ArgoCD with the following commands:

```
#!/bin/bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
kubectl create namespace argocd
# argocd-values.yaml
configs:
  cm:
    admin.enabled: true # -- Enable local admin user
    timeout.reconciliation: 15s # -- Timeout to discover if a new manifests version got published to the repository
    timeout.hard.reconciliation: 0s # -- Timeout to refresh application data as well as target manifests cache
helm upgrade --install argocd argo/argo-cd \
  --namespace argocd -f argocd-values.yaml
# We are setting configs.cm.timeout.reconciliation to 15s
# to reduce the default reconciliation interval (which is 180 seconds) 
# and allow ArgoCD to detect and apply changes more quickly.
# This value is configurable based on your desired sync frequency.
```![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*d_q52zcYaQBAdCmCq1H_yg.gif)

### Step 2— Access the ArgoCD Dashboard and Register Your App Repository

You can access the ArgoCD dashboard by port-forwarding the ArgoCD server service:

```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
kubectl port-forward svc/argocd-server -n argocd 8080:80
```

**Note:** You can manually set or update the ArgoCD `admin` password using the commands below.

```
htpasswd -nbBC 10 "" "yourNewPassword" | tr -d ':\n' | sed 's/$2y/$2a/'
kubectl -n argocd patch secret argocd-secret \
  -p '{"stringData": {
    "admin.password": "$2a$10$1p3WDFDfgfhdfnJQ0xJwahav.nLgZxDOzrJqnK.P0/rxgAoyQFJ3/rWa",
    "admin.passwordMtime": "'$(date +%FT%T%Z)'"
  }}'
kubectl -n argocd rollout restart deployment argocd-server
```

Then, open your browser and navigate to:
👉 [https://localhost:8080](https://localhost:8080)

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*z3Wuh2mHrPU9_cJPj3bmyw.png)

Once logged in, follow the steps I described in my “[previous article](https://medium.com/hedgus/introduction-to-argocd-streamlining-kubernetes-deployments-c2409b8743e9)” to connect your app repository and create a new ArgoCD application pointing to your GitOps deployment manifests.

> This step allows ArgoCD to continuously monitor your manifests and automatically sync updates to your Kubernetes cluster.

### Step 3— Let’s Talk About the GitHub Actions Workflow File

In this step, we’ll define a **CI workflow** that builds and pushes a Docker image to GitHub Container Registry (GHCR) whenever changes are pushed to the `main` branch. This is the first part of our GitOps pipeline, where the application is continuously integrated and containerized.

Here’s a basic structure of the workflow file:

```
name: ArgoCD App
on:
  push:
    branches:
      - main
  # pull_request:
  #   branches:
  #     - main
env:
  IMAGE_NAME: ghcr.io/${{ github.repository }}/app
  GITOPS_REPO: mkanus/argocd-deploy
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout source code
        uses: actions/checkout@v3
      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.repository_owner }}
          password: ${{ secrets.CR_PAT }}
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      - name: Build and push Docker image
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: |
            ${{ env.IMAGE_NAME }}:latest
            ${{ env.IMAGE_NAME }}:${{ github.sha }}
      - name: Update GitOps deployment repo
        run: |
          git clone https://${{ secrets.GITOPS_PAT }}@github.com/${{ env.GITOPS_REPO }} gitops
          cd gitops
          
          # Update the manifest with the latest image tag
          export IMAGE_NAME="${{ env.IMAGE_NAME }}"
          export TAG="${{ github.sha }}"
          sed -i "s|image: ${IMAGE_NAME}:.*|image: ${IMAGE_NAME}:${TAG}|g" deployment.yaml
          # Git Commit and Push Steps
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add deployment.yaml
          git commit -m "Update image to ${{ github.sha }}"
          git push origin main
```

_Under your private app repository, navigate to_ **_Settings > Secrets and variables > Actions_**_, and add the following secret environment variables:_

**_CR_PAT_** _and_ **_GITOPS_PAT_**

_You can assign your own Personal Access Tokens (PATs) with the necessary permissions to these secrets._

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oiYKU5TwlKUpJzzffYpLOQ.png)

### Step 4— Create an ImagePullSecret in the Application Namespace to Access Private Images

Since our repository is private, the container images pushed to GitHub Container Registry (GHCR) are also private by default. To allow Kubernetes to pull these images, we need to create a `**docker-registry**` **type secret** in the application’s namespace.

```
kubectl create secret docker-registry ghcr \
  --docker-server=ghcr.io \
  --docker-username=<your-github-username> \
  --docker-password=<your-personal-access-token> \
  --namespace=<your-app-namespace>
```

### **Step 5— Trigger the CI Pipeline from the Private** `**argocd-app**` **Repository**

Now, let’s trigger the **CI pipeline** from our private `argocd-app` repository.

**_This will start the GitHub Actions workflow, build the Docker image, push it to GHCR, and update the image tag in the GitOps repository._**

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GtTqQ_FUXfYKk5K_Ry5Zmg.gif)

_Thank you for adding my article to your reading list! If you enjoyed it and found it helpful, please consider_ **_following_** _me and giving the article a_ **_clap_**_. Your support means a lot and helps me continue creating content that you love._