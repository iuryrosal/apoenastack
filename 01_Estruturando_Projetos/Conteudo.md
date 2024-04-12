# Roteiro da Aula

## Instalação

Indicado utilizar o WSL: 

Instale o Homebrew. É uma ótima ferramenta para instalação de pacotes no Linux e Mac.
Link do Homebrew: https://brew.sh 

Execute o comando: 
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Após isso, adicione o brew a PATH para conseguir executá-lo por linha de comando no terminal executando esses dois comandos:
```
(echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> /home/iuryrosal/.bashrc

eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```
