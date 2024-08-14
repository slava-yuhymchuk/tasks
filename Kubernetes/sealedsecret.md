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
- `Verify that regular secret was create in tasks namespace:`
  ```bash
  kubectl -n tasks get secret secret-openai -o yaml
  ```
