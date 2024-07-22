- `deploy the sealed-secrets controller`
  ```bash
  kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.27.1/controller.yaml
  ```
- `encrypt regular secret and output to sealedsecret yaml file`
  ```bash
  kubeseal -f secret-openai.yaml -w sealedsecret-openai-dev.yaml
  ```
- `create sealedsecret in tasks namespace`
  ```bash
  kubectl -n tasks create sealedsecret-openai-dev.yaml
  ```
- `verify that sealedsecret was created in tasks namespace`
  ```bash
  kubectl -n tasks get sealedsecret secret-openai -o yaml
  ```
- `verify that regular secret was created in tasks namespace`
  ```bash
  kubectl -n tasks get secret secret-openai -o yaml
  ```
