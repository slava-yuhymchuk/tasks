- `Create argocd namespace:`
  ```bash
  kubectl create ns argocd
  ```
- `Deploy ArgoCD in argocd namespace:`
  ```bash
  kubectl -n argocd apply -f https://raw.githubusercontent.com/argoproj/argo-cd/master/manifests/install.yaml
  ```
- `Configure service type to LoadBalancer:`
  ```bash
  kubectl -n argocd patch svc argocd-server -p '{"spec": {"type": "LoadBalancer"}}'
  ```
- `Get the service hostname:`
  ```bash
  kubectl -n argocd get svc argocd-server -o json | jq -r .status.loadBalancer.ingress[0].hostname
  ```
- `Get the initial admin password:`
  ```bash
  base64 -d <<< `kubectl -n argocd get secret argocd-initial-admin-secret -o json | jq -r .data.password`
  ```
