- `Deploy the sealed-secrets controller:`
  ```bash
  kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.27.1/controller.yaml
  ```
- `Encrypt regular secret and output to sealedsecret yaml file:`
  ```bash
  kubeseal -f secret-openai.yaml -w sealedsecret-openai-dev.yaml
  ```
- `Create sealedsecret in tasks namespace:`
  ```bash
  kubectl -n tasks create -f sealedsecret-openai-dev.yaml
  ```
- `Verify that sealedsecret was created in tasks namespace:`
  ```bash
  kubectl -n tasks get sealedsecret secret-openai -o yaml
  ```
- `Verify that regular secret was created in tasks namespace:`
  ```bash
  kubectl -n tasks get secret secret-openai -o yaml
  ```

- `Import existing certificate to the controller:`
  - `Set variables:`
  ```bash
  export PRIVATEKEY="tls.key"
  export PUBLICKEY="tls.crt"
  export NAMESPACE="kube-system"
  export SECRETNAME="tasks"
  ```
  - `Create a TLS K8s secret using your own RSA key pair:`
  ```bash
  kubectl -n "$NAMESPACE" create secret tls "$SECRETNAME" --cert="$PUBLICKEY" --key="$PRIVATEKEY"
  kubectl -n "$NAMESPACE" label secret "$SECRETNAME" sealedsecrets.bitnami.com/sealed-secrets-key=active
  ```
  - `Delete the controller pod to pick the new keys:`
  ```bash
  kubectl -n "$NAMESPACE" delete pod -l name=sealed-secrets-controller
  ```
  - `See the new certificate in controller logs:`
  ```bash
  kubectl -n "$NAMESPACE" logs -l name=sealed-secrets-controller
  ```
