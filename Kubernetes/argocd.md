kubectl create ns argocd
kubectl -n argocd apply -f https://raw.githubusercontent.com/argoproj/argo-cd/master/manifests/install.yaml
kubectl -n argocd patch svc argocd-server -p '{"spec": {"type": "LoadBalancer"}}'
base64 -d <<< `kubectl -n argocd get secret argocd-initial-admin-secret -o json | jq -r .data.password`