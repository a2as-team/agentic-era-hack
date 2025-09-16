Argo CD
=======

[![manojkumar](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*zrIS5rlpePQTTCv9)](https://medium.com/@akulamanojkumar988?source=post_page---byline--a909b5c62acb---------------------------------------)

[manojkumar](https://medium.com/@akulamanojkumar988?source=post_page---byline--a909b5c62acb---------------------------------------)

13 min read

·

Mar 6, 2024

[nameless link](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fa909b5c62acb&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40akulamanojkumar988%2Fargo-cd-a909b5c62acb&user=manojkumar&userId=100b6452cd9c&source=---header_actions--a909b5c62acb---------------------clap_footer------------------)

--

1

[nameless link](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa909b5c62acb&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40akulamanojkumar988%2Fargo-cd-a909b5c62acb&source=---header_actions--a909b5c62acb---------------------bookmark_footer------------------)

Listen

Share

A Complete Overview of ArgoCD with a Practical Example……………
-----------------------------------------------------------

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*VCEyv5SL8UbKYiP2.png)

Content:
--------

01, Introduction to Argo CD
---------------------------

02, Key Features and Benefits
-----------------------------

03,Practical Implementation and Case Studies
--------------------------------------------

Introduction to Argo CD
-----------------------

![captionless image](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*L2QozZIcqGF2wHGHIDfp7A.png)

What is ArgoCD?
---------------

Argo CD is a Kubernetes-native continuous deployment (CD) tool. Unlike external CD tools that only enable push-based deployments, Argo CD can pull updated code from Git repositories and deploy it directly to Kubernetes resources.

What is GitOps?
---------------

GitOps is a way of implementing Continuous Deployment for cloud-native applications. It focuses on a developer-centric experience when operating infrastructure, by using tools developers are already familiar with, including Git and Continuous Deployment tools.

The core idea of GitOps is to have a Git repository that always contains declarative descriptions of the infrastructure currently desired in the production environment and an automated process to make the production environment match the described state in the repository. If you want to deploy a new application or update an existing one, you only need to update the repository — the automated process handles everything else. It’s like having cruise control for managing your applications in production.

Core Functionality of Argo CD
-----------------------------

01)Continuous Monitoring
------------------------

Argo CD continuously monitors running applications and compares the current state with the desired state defined in the Git repository. Any variances are automatically reconciled to maintain the desired state.

02)Declarative Application Management
-------------------------------------

It enables declarative definitions of applications and their configurations, ensuring that the desired state is maintained without the need for manual intervention.

03)GitOps Approach
------------------

Argo CD follows the GitOps methodology, where application definitions, configurations, and environments are versioned in a Git repository, providing a clear audit trail and ensuring consistency.

Use Cases and Adoption
----------------------

01)Enterprise Adoption
----------------------

Argo CD has gained significant traction in enterprise environments due to its ability to streamline and automate the deployment and management of complex Kubernetes applications.

02)Community Support
--------------------

The tool benefits from a vibrant and active community, contributing to its evolution and the development of best practices for continuous delivery in Kubernetes.

03)Integration Flexibility
--------------------------

Argo CD integrates seamlessly with various CI/CD tools, version control systems, and Kubernetes distributions, making it a versatile choice for organizations with diverse tech stacks.

Argo CD Architecture
--------------------

01)Controller and API Server
----------------------------

The core of Argo CD’s architecture consists of the controller and API server, responsible for managing the application deployment and providing the user interface.

02)Application Set Controller
-----------------------------

This component enables the management of multiple applications as a single entity, allowing for efficient and scalable management of complex application landscapes.

03)Repository and Synchronization
---------------------------------

Argo CD interacts directly with the Git repository to synchronize the desired state with the live state of applications, ensuring consistency and reliability.

Key efits Features and Ben
--------------------------

GitOps Principles and Best Practices
------------------------------------

01)Declarative Configuration
----------------------------

Argo CD enforces the GitOps principle of declarative configuration, ensuring that the desired state of applications is explicitly defined and versioned in a Git repository.

02)Automated Synchronization
----------------------------

The tool automates the synchronization of the live state with the desired state, reducing the risk of configuration drift and ensuring consistency across environments.

03)Auditability and Traceability
--------------------------------

By leveraging Git as the source of truth, Argo CD provides a transparent audit trail and traceability for all changes made to application configurations.

Application Health and Rollback
-------------------------------

01)Health Status Monitoring
---------------------------

Argo CD continuously monitors the health and status of applications, providing real-time insights into their operational state and performance.

02)Automated Rollback
---------------------

In the event of application failures or deviations from the desired state, Argo CD facilitates automated rollbacks to restore the application to a stable and consistent state.

03)Customizable Health Checks
-----------------------------

It offers customizable health checks and validation mechanisms, allowing organizations to define specific criteria for application health and performance.

Scalability and Multi-Tenancy
-----------------------------

01)Scalable Application Management
----------------------------------

Argo CD supports the management of large-scale, complex application landscapes, providing the scalability required for enterprise-grade continuous delivery.

02)Multi-Tenancy Support
------------------------

It offers robust multi-tenancy capabilities, allowing organizations to manage and deploy applications across diverse teams and environments with distinct access controls and permissions.

03)Resource Quotas and Limits
-----------------------------

Argo CD enables the enforcement of resource quotas and limits, ensuring efficient resource utilization and allocation across applications and environments.

Security and Compliance
-----------------------

01)Role-Based Access Control (RBAC)
-----------------------------------

The tool provides fine-grained RBAC, allowing organizations to define granular access controls and permissions for different user roles and responsibilities.

02)Secrets Management
---------------------

Argo CD offers secure and centralized secrets management, ensuring that sensitive information such as credentials and API tokens are handled with the utmost security.

03)Compliance Automation
------------------------

It facilitates compliance automation by enforcing best practices, security policies, and regulatory requirements through automated configuration management and validation.

Practical Implementation and Case Studies
-----------------------------------------

GitOps Principles and Best Practices
------------------------------------

01)Declarative Configuration
----------------------------

Argo CD enforces the GitOps principle of declarative configuration, ensuring that the desired state of applications is explicitly defined and versioned in a Git repository.

02)Automated Synchronization
----------------------------

The tool automates the synchronization of the live state with the desired state, reducing the risk of configuration drift and ensuring consistency across environments.

03)Auditability and Traceability
--------------------------------

By leveraging Git as the source of truth, Argo CD provides a transparent audit trail and traceability for all changes made to application configurations.

Application Health and Rollback
-------------------------------

01)Health Status Monitoring
---------------------------

Argo CD continuously monitors the health and status of applications, providing real-time insights into their operational state and performance.

02)Automated Rollback
---------------------

In the event of application failures or deviations from the desired state, Argo CD facilitates automated rollbacks to restore the application to a stable and consistent state.

03)Customizable Health Checks
-----------------------------

It offers customizable health checks and validation mechanisms, allowing organizations to define specific criteria for application health and performance.

Scalability and Multi-Tenancy
-----------------------------

01)Scalable Application Management
----------------------------------

Argo CD supports the management of large-scale, complex application landscapes, providing the scalability required for enterprise-grade continuous delivery.

02)Multi-Tenancy Support
------------------------

It offers robust multi-tenancy capabilities, allowing organizations to manage and deploy applications across diverse teams and environments with distinct access controls and permissions.

03)Resource Quotas and Limits
-----------------------------

Argo CD enables the enforcement of resource quotas and limits, ensuring efficient resource utilization and allocation across applications and environments.

Security and Compliance
-----------------------

01)Role-Based Access Control (RBAC)
-----------------------------------

The tool provides fine-grained RBAC, allowing organizations to define granular access controls and permissions for different user roles and responsibilities.

02)Secrets Management
---------------------

Argo CD offers secure and centralized secrets management, ensuring that sensitive information such as credentials and API tokens are handled with the utmost security.

03)Compliance Automation
------------------------

It facilitates compliance automation by enforcing best practices, security policies, and regulatory requirements through automated configuration management and validation.

Practical Implementation and Case Studies
-----------------------------------------

Implementing Argo CD in a Kubernetes Environment
------------------------------------------------

![captionless image](https://miro.medium.com/v2/resize:fit:1350/format:webp/0*gYUDPEWAye1VXus4)

01)Installation and Configuration
---------------------------------

A step-by-step guide to installing and configuring Argo CD in a Kubernetes cluster, including the setup of applications and repositories.

![captionless image](https://miro.medium.com/v2/resize:fit:600/format:webp/0*fA8RAJkymPGFkp2d)

02)Best Practices
-----------------

Practical recommendations and best practices for leveraging Argo CD to achieve efficient and reliable continuous delivery in Kubernetes environments.

![captionless image](https://miro.medium.com/v2/resize:fit:1350/format:webp/0*Xq_ERxqsgKvBDGfV)

03)Demonstration
----------------

A live demonstration showcasing the deployment and management of applications using Argo CD, highlighting its key features and capabilities.

Case Study: Streamlining Continuous Delivery with Argo CD
---------------------------------------------------------

01)Organizational Context
-------------------------

An overview of how a hypothetical organization implemented Argo CD to streamline its continuous delivery processes and enhance application deployment efficiency.

02)Challenges and Solutions
---------------------------

A detailed exploration of the challenges faced by the organization and how Argo CD provided solutions to address these challenges effectively.

03)Outcomes and Benefits
------------------------

Insights into the tangible outcomes and benefits realized by the organization after adopting Argo CD, including improvements in deployment speed, reliability, and scalability.

Real-World Applications and Success Stories
-------------------------------------------

01)Industry Use Cases
---------------------

An analysis of real-world applications of Argo CD across diverse industries, showcasing how organizations have leveraged the tool to achieve their continuous delivery goals.

02)Success Stories
------------------

Case studies highlighting the success stories of organizations that have embraced Argo CD, illustrating the transformative impact of the tool on their application deployment and management practices.

03)Lessons Learned
------------------

Key lessons and insights drawn from the experiences of organizations that have implemented Argo CD, providing valuable takeaways for the audience.

Future Trends and Innovations in Argo CD
----------------------------------------

01)Evolution of Argo CD
-----------------------

A glimpse into the future of Argo CD, exploring potential advancements, feature enhancements, and innovations that are poised to shape the tool’s evolution.

02)Community Contributions
--------------------------

Insights into the role of the community in driving the evolution of Argo CD, including contributions, feedback mechanisms, and collaborative initiatives.

03)Opportunities for Innovation
-------------------------------

An exploration of the emerging trends and opportunities for innovation in the realm of continuous delivery, with a focus on how Argo CD is positioned to embrace these developments.

Example:
--------

How to achieve GitOps using Argo CD?
------------------------------------

Every enterprise uses Git as its source code management software to store code. Developers can commit their infrastructure configurations, such as Kubernetes resources definition, in Git to create environments needed for application deployment.

Once a developer implements a feature ( with a new application and K8S configurations) and merges with the main branch, the CI process is initiated for generating and testing an image.

After the review and approval of the application, the pull request in Git is merged with the main branch. With the help of the GitOps agent, Argo CD will immediately identify the new versions of a configuration that was recently merged and compare it with the running application in the destination environment (it can be pre-prod or prod).

In case of a mismatch, it highlights out-of-sync status, and in the backend, Argo CD uses the Kubernetes controller to reconcile the new changes to cluster resources. Once the Kubernetes resources are ready, it informs the user the application is in sync.

Argo CD also uses an agent to constantly monitor the end environment and check its status with Git. Argo CD synchronizes the current state with the declared state of configurations and ensures that new configurations are correctly deployed to a Kubernetes cluster.

As all the records of all changes, including all details of the environment, at every stage of the process are stored in Git, Argo CD helps roll back applications to previous states in a single click.

Benefits of Argo CD:
--------------------

1.  **Improve developer productivity**

Argo CD provides developers with a self-service environment for application deployment. Software development teams can focus on creativity and writing business logic instead of time and energy on manual and remedial deployments.

**2. Improved software delivery compliance**

Allow your developers, Ops, and DevOps teams to use a single platform for infrastructure change management. Apply organizational policies to restrict access to Kubernetes resources and minimize your application downtime and outages.

**3. Increased collaboration in SDLC**

While working on Argo CD, every team member can work from the same system to achieve GitOps and understand the status of individual processes. The single Git repository fosters collaboration amongst team members by assigning tasks to individuals and deploying code from each person as necessary.

**4. Faster deployments**

Argo CD allows teams to perform more rapid deployments into Kubernetes clusters across multi-cloud. Quicker releases of application changes mean shorter time to market and more flexibility in responding to customer demand.

Prerequisites:
--------------

*   A running Kubernetes cluster

How to install ArgoCD?
----------------------

*   For this tutorial, you must have a running kubernetes cluster like I have minikube running on my server.
*   **Create the namespace for argoCD**

```
kubectl create namespace argocd
```

*   **Install ArgoCD using the below command**

```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

*   **After installing the ArgoCD, you can run the below command to check what resources it has created.**

```
ubuntu@ip-172-31-7-106:~$ kubectl get all -n argocd
NAME                                                    READY   STATUS    RESTARTS   AGE
pod/argocd-application-controller-0                     1/1     Running   0          106m
pod/argocd-applicationset-controller-787bfd9669-4mxq6   1/1     Running   0          106m
pod/argocd-dex-server-bb76f899c-slg7k                   1/1     Running   0          106m
pod/argocd-notifications-controller-5557f7bb5b-84cjr    1/1     Running   0          106m
pod/argocd-redis-b5d6bf5f5-482qq                        1/1     Running   0          106m
pod/argocd-repo-server-56998dcf9c-c75wk                 1/1     Running   0          106m
pod/argocd-server-5985b6cf6f-zzgx8                      1/1     Running   0          106m
NAME                                              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
service/argocd-applicationset-controller          ClusterIP   10.102.163.101   <none>        7000/TCP,8080/TCP            106m
service/argocd-dex-server                         ClusterIP   10.101.227.215   <none>        5556/TCP,5557/TCP,5558/TCP   106m
service/argocd-metrics                            ClusterIP   10.111.59.189    <none>        8082/TCP                     106m
service/argocd-notifications-controller-metrics   ClusterIP   10.96.102.185    <none>        9001/TCP                     106m
service/argocd-redis                              ClusterIP   10.97.229.117    <none>        6379/TCP                     106m
service/argocd-repo-server                        ClusterIP   10.102.16.58     <none>        8081/TCP,8084/TCP            106m
service/argocd-server                             ClusterIP   10.98.71.135     <none>        80/TCP,443/TCP               106m
service/argocd-server-metrics                     ClusterIP   10.109.248.207   <none>        8083/TCP                     106m
NAME                                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/argocd-applicationset-controller   1/1     1            1           106m
deployment.apps/argocd-dex-server                  1/1     1            1           106m
deployment.apps/argocd-notifications-controller    1/1     1            1           106m
deployment.apps/argocd-redis                       1/1     1            1           106m
deployment.apps/argocd-repo-server                 1/1     1            1           106m
deployment.apps/argocd-server                      1/1     1            1           106m
NAME                                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/argocd-applicationset-controller-787bfd9669   1         1         1       106m
replicaset.apps/argocd-dex-server-bb76f899c                   1         1         1       106m
replicaset.apps/argocd-notifications-controller-5557f7bb5b    1         1         1       106m
replicaset.apps/argocd-redis-b5d6bf5f5                        1         1         1       106m
replicaset.apps/argocd-repo-server-56998dcf9c                 1         1         1       106m
replicaset.apps/argocd-server-5985b6cf6f                      1         1         1       106m
NAME                                             READY   AGE
statefulset.apps/argocd-application-controller   1/1     106m
ubuntu@ip-172-31-7-106:~$
```

*   **Now in order to access the UI of ArgoCD, you need to run the below command**

```
kubectl port-forward --address 0.0.0.0 svc/argocd-server -n argocd 8080:443
```

*   The above command will forward port 8080 and map it with the argocd-server service’s 443 port.
*   You can check the UI of ArgoCD by visiting `localhost:8080` or `ip-of-server:8080`
*   Now, in order to log into the UI you need the credentials. So, for a username, you can write `admin` and the password is stored in the secret called `argocd-initial-admin-secret` in the cluster.
*   You need to run the below command to get the value of the secret.

```
kubectl get secret argocd-initial-admin-secret -n argocd -o yaml
```

*   The secret base64 encoded so, you have to decode the secret by running the below command.

```
echo "secret" | base64 decode
```

*   After running the above command you can have the decoded value of the secret and using that as a password you can log in to the UI.
*   Now, the installation has been completed.

Now, the installation is completed.

So, now I have an application running on my kubernetes cluster. Below are the manifest files for that.

1.  **Deployment file**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  selector:
    matchLabels:
      app: myapp
  replicas: 4
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: dhruvin30/dhsoniweb
```

*   I am using `dhsoniweb` which is my portfolio website’s docker image.

**2. Service file**

```
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
  - port: 80
    protocol: TCP
    targetPort: 8080
```

And I have stored the code in [**this**](https://github.com/DhruvinSoni30/ArgoCD-Demo) repository.

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*e0a563SrY8yvp_XU.png)

Repository

So, now in order for argoCD to sync with this repository we need to write some manifest file for that. Here is the manifest file for that.

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp-argo-application
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/DhruvinSoni30/ArgoCD-Demo.git
    targetRevision: HEAD
    path: dev
  destination: 
    server: https://kubernetes.default.svc
    namespace: myapp
  syncPolicy:
    syncOptions:
    - CreateNamespace=true
    automated:
      selfHeal: true
      prune: true
```

*   `argoproj.io/v1alpha1` is an API version of argoCD. The API Version might get changed once argoCD has some new release. Always refer to the documentation for the latest information.
*   I am defining my repository URL in `repoURL` section.
*   `targetRevision` is set to HEAD so that it will always fetch the latest commit.
*   `path` is set to `dev` because I have my application’s manifest files in `dev` folder.
*   In the `destination` section we have `server` section and it is set to `https://kubernetes.default.svc` which is the internal service of the kubernetes API Server.

```
ubuntu@ip-172-31-7-106:~$ kubectl get svc 
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   137m
ubuntu@ip-172-31-7-106:~$
```

*   `namespace` is set to `myapp` , because we want to create our application in that namespace. Now, we actually don’t have the namespace already created because we want argoCD to create that automatically.
*   In order for argoCD to create the namespace automatically we need to define the below attributes.

```
syncPolicy:
    syncOptions:
    - CreateNamespace=true
```

*   We want argoCD to automatically sync any changes in the git repository but by default, it is turned off. So in order to enable that we need to define the below attributes.

```
automated:
  selfHeal: true
  prune: true
```

*   If you apply any changes from the backend using `kubectl` utility then we want to override that with whatever we have in our git repository in order to do that we have `selfHeal: true` for that.
*   If we rename any component or delete the entire component then we want argoCD to delete that component in the cluster as well and in order to do that we have `prune: true` for that.
*   argoCD will check the changes in the git repository every 3 minutes. If you want argoCD to check the changes as soon as it has done then you can implement the webhook for that.
*   Now, that we have our file ready we need to run the below command to apply that.

```
kubectl apply -f application.yaml
```

*   Once you apply the file you can check your application in the UI.

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Ocrj3J53nr5DhYv0.png)

Application

*   You can click on your application and check the various details.

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*cHVxc4EpmYAg9Joc.png)

Workflow

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*5Fnzfj8orUgiJLQu.png)

Manifest file

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*mKbHSiirlodonQzw.png)

Manifest file

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*sy6x49Ower52mgV2.png)

Events of pod creation

*   Now let’s say you want to increase the replica for your application. You just need to commit your changes in the git repository like below and argoCD will take care of the further actions.

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*klBDq7Fbw32i8fcV.png)

Changes

*   As soon as you commit the changes in the repository, argoCD will look for the changes and apply the changes in the cluster.

![captionless image](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*8dby7abWLnT83rIx.png)

Changes in cluster

*   As you can see, now we have a total of 4 pods in the cluster.

```
ubuntu@ip-172-31-7-106:~$ kubectl get pods -n myapp
NAME                                READY   STATUS    RESTARTS   AGE
myapp-deployment-544dd58bc4-4sntz   1/1     Running   0          13h
myapp-deployment-544dd58bc4-wkf5j   1/1     Running   0          13h
myapp-deployment-544dd58bc4-xt7hb   1/1     Running   0          13h
myapp-deployment-544dd58bc4-zjmn8   1/1     Running   0          13h
ubuntu@ip-172-31-7-106:~$
```

*   Now you can perform different changes as per your need and argoCD will take care of the further action.

Thank You
---------

Contact: akulamanojkumar988@gmail.com

Linkedin ID: [www.linkedin.com/in/manoj-kumar-akula-792706241](http://www.linkedin.com/in/manoj-kumar-akula-792706241)