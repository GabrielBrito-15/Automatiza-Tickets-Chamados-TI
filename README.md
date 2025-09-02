# Automatização de Criação de Chamados (Power Automate)

Este repositório documenta, em **formato de código**, o fluxo de automatização de criação de chamados
integrando **Microsoft Teams** e **Office 365**. O objetivo é facilitar a publicação no GitHub e a
colaboração técnica da equipe.

> Baseado no documento interno "Apresentação do Fluxo de Automatização" (11 de agosto de 2025).

## Visão Geral

- **Disparo**: menções de palavras-chave no Microsoft Teams.
- **Coleta de dados**: mensagem pai, detalhes do autor (Office 365) e metadados da mensagem.
- **Notificação**: construção de assunto/corpo e envio de e-mail (Outlook 365).
- **Acompanhamento**: atraso controlado e leitura de e-mails para verificar respostas/atualizações.
- **Gestão de tickets**: extração/geração de ID e confirmação no Teams.

## Estrutura

```
.
├── README.md
├── flow_spec.yaml        # Especificação do fluxo (legível por humanos)
└── src
    └── flow.py           # Pseudocódigo de referência (Python)
```

## Como usar

1. Leia o `flow_spec.yaml` para entender as etapas e integrações.
2. Use o `src/flow.py` como **pseudocódigo** de referência para orientar a implementação no Power Automate
   ou em integrações personalizadas.
3. Abra _Issues_ para discutir melhoria de regras de filtragem, logs e observabilidade.

## Recomendações

- Adicionar condições para filtrar e-mails irrelevantes (ex.: regras por assunto/remetente).
- Persistir **ID do ticket** em um banco (SharePoint, Dataverse, SQL) para rastreabilidade.
- Configurar **alertas de erro** e telemetria.
- Testar cada etapa para garantir passagem correta de dados entre ações.

## Licença

MIT
