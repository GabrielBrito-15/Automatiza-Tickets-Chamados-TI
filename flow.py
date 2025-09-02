"""
Pseudocódigo em Python para ilustrar a lógica de alto nível do fluxo.
Isto NÃO substitui o Power Automate, mas ajuda a alinhar regras, dados e integrações.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import re
import time

@dataclass
class TeamsMentionEvent:
    message_id: str
    team_id: str
    channel_id: str
    author_user_id: str
    mentioned_keywords: List[str]

@dataclass
class User:
    display_name: str
    mail: str

@dataclass
class Message:
    id: str
    text: str
    metadata: Dict[str, Any]
    parent: Optional[Dict[str, Any]] = None

def on_keyword_mention(event: TeamsMentionEvent):
    """
    Disparo do fluxo: executado quando há menção de palavra-chave no Teams.
    """
    for _ in event.mentioned_keywords:
        parent = get_parent_message(event.message_id)
        user = get_user_details(event.author_user_id)
        msg = get_message_details(event.message_id)

        subject = f"[Ticket] Nova solicitação via Teams - {user.display_name}"
        body = (
            "Origem: Teams\n"
            f"Autor: {user.display_name} <{user.mail}>\n"
            f"Texto: {msg.text}\n"
            f"Metadados: {msg.metadata}"
        )

        send_email("suporte@empresa.com", subject, body)

        delay_seconds(120)  # Exemplo: 2 minutos; ajuste conforme necessário

        emails = get_emails(query="subject:'Nova solicitação via Teams' newer_than:1d")
        ticket_id = extract_ticket_id_from_emails(emails) or "TICKET-PENDENTE"

        post_confirmation_to_teams(
            channel_id=event.channel_id,
            reply_to_message_id=event.message_id,
            text=f"✅ Ticket {ticket_id} criado/atualizado para a sua solicitação."
        )

def get_parent_message(message_id: str) -> Dict[str, Any]:
    # Placeholder para chamada Microsoft Teams
    return {"id": "parent-of-" + message_id}

def get_user_details(user_id: str) -> User:
    # Placeholder para Office 365 Users
    return User(display_name="Usuário Exemplo", mail="usuario@empresa.com")

def get_message_details(message_id: str) -> Message:
    # Placeholder para Microsoft Teams
    return Message(id=message_id, text="Texto da mensagem de gatilho", metadata={"source": "teams"})

def send_email(to: str, subject: str, body: str):
    # Placeholder para Outlook Office 365 (V2)
    print(f"Enviando e-mail para {to} | Assunto: {subject}\n{body}\n")

def delay_seconds(seconds: int):
    # Placeholder para 'Delay' (não dormir de verdade em produção)
    time.sleep(0)  # no-op para evitar atrasos reais aqui

def get_emails(query: str) -> List[Dict[str, Any]]:
    # Placeholder para Outlook Office 365 (Get emails V3)
    return [
        {"subject": "Re: [Ticket] Nova solicitação via Teams - Usuário Exemplo (Ticket 123)"},
        {"subject": "Atualização: [Ticket] Nova solicitação via Teams - Usuário Exemplo - Ticket 456"},
    ]

def extract_ticket_id_from_emails(emails: List[Dict[str, Any]]) -> Optional[str]:
    pattern = re.compile(r"Ticket\s*(\d+)", re.IGNORECASE)
    for e in emails:
        m = pattern.search(e.get("subject", ""))
        if m:
            return m.group(1)
    return None

def post_confirmation_to_teams(channel_id: str, reply_to_message_id: str, text: str):
    # Placeholder para postar resposta no Teams
    print(f"Postando no Teams (canal {channel_id}) em resposta a {reply_to_message_id}: {text}")
