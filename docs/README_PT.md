[English](README.md) || **Português (Brasil)**

<p align="center">
  <img width="220" height="auto" src="cubic_logo.png">
    <br/><strong>Cubic AdBlock</strong></b>
</p>

<p align="center">
  <img alt="Versão Atual no GitHub" src="https://img.shields.io/github/v/release/Vaz15K/Cubic-AdBlock">
  <img alt="Downloads do GitHub (todos os ativos, todos os lançamentos)" src="https://img.shields.io/github/downloads/Vaz15K/Cubic-AdBlock/total">
  <img alt="Status do fluxo de trabalho do GitHub" src="https://img.shields.io/github/actions/workflow/status/Vaz15K/Cubic-AdBlock/update_hosts.yml">
  <img alt="GitHub Licença" src="https://img.shields.io/github/license/Vaz15K/Cubic-AdBlock">
</p>

Um módulo simples de AdBlock baseado no arquivo hosts.

- Alguns links são permitidos para que você possa usar alguns serviços essenciais, como login no Facebook, APIs do Google e Microsoft, serviços da Samsung e outros.
- Se um aplicativo não estiver funcionando, você pode fazer uma solicitação para permiti-lo, desde que não esteja relacionado a publicidade.

> [!NOTE]
> O arquivo hosts tem aproximadamente 33 MB de tamanho. \
> O módulo é atualizado semanalmente.

## Como instalar
Instalar o módulo é muito simples.

1. **Baixe o [módulo mais recente](https://github.com/Vaz15k/Cubic-AdBlocker/releases)**
> O módulo também está disponível no [**MMRL**](https://mmrl.dergoogler.com)
2. **Instale com seu gerenciador de root preferido**

## Usando com Adaway
Uma alternativa ao módulo é usar o aplicativo [Adaway](https://adaway.org), que permite editar o arquivo com extrema facilidade. \
Recomendo usar o Adaway se você quiser permitir anúncios em um aplicativo específico.

> Não recomendo editar o arquivo hosts diretamente devido ao seu tamanho e ao número de linhas, que podem conter links semelhantes ao que você deseja desbloquear. \
> Você também pode desativar o módulo temporariamente e depois ativá-lo, mas teria que reiniciar o dispositivo.

Para usar essa lista no AdAway, adicione o seguinte URL à lista de repositórios no aplicativo:
```
https://raw.githubusercontent.com/Vaz15k/Cubic-AdBlocker/cubic/module/system/etc/hosts
```
- Para usuários do Magisk: habilite o módulo "Systemless hosts" nas configurações.
- Para usuários do APatch ou KernelSU: use o módulo [Systemless Hosts KSU](https://github.com/symbuzzer/systemless-hosts-KernelSU-module).

> [!NOTE]
> Se quiser, você pode usar o Adaway no modo VPN, assim você não precisará de root.

## Créditos
Este módulo tem seus hosts baseados nas listas abaixo, **Agradecimentos Especiais** para:

- [StevenBlack](https://github.com/StevenBlack/hosts)
- [NoTrack Block Lists](https://gitlab.com/quidsup/notrack-blocklists)
- [GoodbyeAds](https://github.com/jerryn70/GoodbyeAds)
- [1 Hosts](https://o0.pages.dev)
- [Peter Lowe](https://pgl.yoyo.org/adservers)
- [HaGeZi](https://github.com/hagezi/dns-blocklists)
