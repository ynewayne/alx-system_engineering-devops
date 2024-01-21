# 0x0B. Simplifying SSH

## Resources

- [What is a (physical) server - text](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)
- [What is a (physical) server - video](https://www.youtube.com/watch?v=B1ANfsDyjeA)
- [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
- [SSH Config File](https://www.ssh.com/academy/ssh/config)
- [Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)
- [How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58)
- [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc) (*Long, but highly informative. Consider watching at x1.25 speed or above.*)

## Tasks

<details>
<summary>[Task 0: Use a private key](./0-use_a_private_key)</summary><br>
![Image](https://i.postimg.cc/yW4gBSpM/image.png)
</details>

<details>
<summary>[Task 1: Create an SSH key pair](./1-create_ssh_key_pair)</summary><br>
![Image](https://i.postimg.cc/pXPbpdbx/image.png)
</details>

<details>
<summary>[Task 2: Client configuration file](./2-ssh_config)</summary><br>
![Image](https://i.postimg.cc/y6brchGV/image.png)
</details>

<details>
<summary>[Task 3: Let me in!](#)</summary><br>
![Image](https://i.postimg.cc/3N2k9F3k/image.png)
</details>

<details>
<summary>[Task 4: Client configuration file (w/ Puppet)](./100-puppet_ssh_config.pp)</summary><br>
![Image](https://i.postimg.cc/ryBvRXzV/image.png)<br>
- Install puppet stdlib module:
  ```
  sudo puppet module install puppetlabs-stdlib
  ```
</details>
