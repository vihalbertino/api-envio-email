import json
from pathlib import Path
from datetime import datetime
from html import escape


STATUS = {
    "0": "Normal",
    "1": "Em investigação",
    "3": "Resolvido"
}


def create_health_email(file_path: str, file_name: str):

    caminho_arquivo = Path(file_path) / file_name

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        eventos = json.load(arquivo)

    html = """
    <html>
        <body style="font-family: Arial, sans-serif; background-color: #f4f6f8; padding: 20px;">

            <div style="
                max-width: 900px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
            ">

                <h2 style="margin-bottom: 5px;">
                    AWS Health Monitor
                </h2>

                <p>
                    Eventos encontrados na última coleta:
                    <strong>{}</strong>
                </p>

    """.format(len(eventos))

    for evento in eventos:

        status = STATUS.get(str(evento["status"]), f"Status {evento['status']}")

        data_evento = datetime.fromtimestamp(
            int(evento["date"])
        ).strftime("%d/%m/%Y %H:%M:%S")

        html += f"""
                <div style="
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    padding: 20px;
                    margin-top: 20px;
                ">

                    <h3>{escape(evento['service_name'])}</h3>

                    <p>
                        <strong>Resumo:</strong>
                        {escape(evento['summary'])}
                    </p>

                    <p>
                        <strong>Região:</strong>
                        {escape(evento['region_name'])}
                    </p>

                    <p>
                        <strong>Status:</strong>
                        {escape(status)}
                    </p>

                    <p>
                        <strong>Data:</strong>
                        {data_evento}
                    </p>

                    <hr>

                    <h4>Histórico</h4>

        """

        for log in evento["event_log"]:

            timestamp = datetime.fromtimestamp(
                int(log["timestamp"])
            ).strftime("%d/%m/%Y %H:%M:%S")

            html += f"""
                    <div style="
                        margin-bottom: 15px;
                        padding: 10px;
                        background: #f8f9fa;
                        border-radius: 5px;
                    ">
                        <strong>{escape(log['summary'])}</strong><br>
                        {escape(log['message'])}<br>
                        <small>{timestamp}</small>
                    </div>
            """

        html += """
                </div>
        """

    html += """
            </div>
        </body>
    </html>
    """

    assunto = f"AWS Health Monitor - {len(eventos)} evento(s)"

    return assunto, html