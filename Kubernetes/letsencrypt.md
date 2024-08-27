- `Install Certbot:`
  ```bash
  sudo apt install certbot
  ```
- `Run Certbot with manual mode:`
  ```bash
  sudo certbot certonly --manual --preferred-challenges dns --cert-name devsecops15.com
  ```
- `Follow on-screen instructions`
- `Create DNS TXT records`
- `Create K8s TLS secret manifests from the generated certificate files`
  ```bash
  kubectl create secret tls secret-tls --cert=fullchain.pem --key=privkey.pem --dry-run=client -o yaml > secret-tls.yaml
  ```
