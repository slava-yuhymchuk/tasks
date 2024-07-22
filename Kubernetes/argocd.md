<!-- create argocd namespace -->
kubectl create ns argocd
<!-- deploy ArgoCD in argocd namespace -->
kubectl -n argocd apply -f https://raw.githubusercontent.com/argoproj/argo-cd/master/manifests/install.yaml
<!-- configure service type to LoadBalancer -->
kubectl -n argocd patch svc argocd-server -p '{"spec": {"type": "LoadBalancer"}}'
<!-- get the service hostname -->
kubectl -n argocd get svc argocd-server -o json | jq -r .status.loadBalancer.ingress[0].hostname
<!-- get the initial admin password -->
base64 -d <<< `kubectl -n argocd get secret argocd-initial-admin-secret -o json | jq -r .data.password`