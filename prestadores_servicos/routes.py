from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for

prestador_bp = Blueprint("prestadores_servicos", __name__)

PRESTADORES_DB = {
    1: {
        "id": 1,
        "cnpj": "12.345.678/0001-00",
        "razao_social": "Solar Manutenções LTDA",
        "telefone": "(83) 3333-1111",
        "email": "atendimento@solarmaint.com",
        "endereco": "Av. Brasil, 500",
        "site": "www.solarmaint.com",
        "chave_pix": "12345678000100",
        "status": "Ativo",
        "data_alteracao_status": "2026-10-05 09:15:00",
    }
}

ORDENS_SERVICO_DB = [
    {
        "id": 101,
        "prestador_id": 1,
        "descricao": "Manutenção Preventiva Inversor 01",
        "data_abertura": "2026-09-10",
        "status": "Concluída",
    },
    {
        "id": 102,
        "prestador_id": 1,
        "descricao": "Limpeza de Painéis Solares Usina 02",
        "data_abertura": "2026-10-12",
        "status": "Em Andamento",
    },
]


@prestador_bp.route("/", methods=["GET"])
def listar_prestadores():
    termo = request.args.get("termo", "").strip().lower()
    status_filtro = request.args.get("status", "").strip()

    resultados = list(PRESTADORES_DB.values())

    if termo:
        resultados = [
            p
            for p in resultados
            if termo in p["razao_social"].lower() or termo in p["cnpj"].lower()
        ]

    if status_filtro:
        resultados = [
            p
            for p in resultados
            if p["status"].lower() == status_filtro.lower()
        ]

    return render_template(
        "prestadores_servicos/index.html", prestadores=resultados
    )


@prestador_bp.route("/novo", methods=["GET", "POST"])
def criar_prestador():
    if request.method == "POST":
        cnpj = request.form.get("cnpj", "").strip()
        razao_social = request.form.get("razao_social", "").strip()
        telefone = request.form.get("telefone", "").strip()
        email = request.form.get("email", "").strip()
        endereco = request.form.get("endereco", "").strip()
        status = request.form.get("status", "Ativo").strip()
        site = request.form.get("site", "").strip()
        chave_pix = request.form.get("chave_pix", "").strip()

        if not (cnpj and razao_social and telefone and email and endereco and status):
            flash("Campos obrigatórios não preenchidos", "danger")
            return render_template("prestadores_servicos/form.html"), 400

        for p in PRESTADORES_DB.values():
            if p["cnpj"] == cnpj:
                flash(
                    "CNPJ já cadastrado para outro prestador", "danger"
                )
                return render_template("prestadores_servicos/form.html"), 400

        novo_id = (
            max(PRESTADORES_DB.keys(), default=0) + 1 if PRESTADORES_DB else 1
        )

        PRESTADORES_DB[novo_id] = {
            "id": novo_id,
            "cnpj": cnpj,
            "razao_social": razao_social,
            "telefone": telefone,
            "email": email,
            "endereco": endereco,
            "site": site,
            "chave_pix": chave_pix,
            "status": status,
            "data_alteracao_status": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        flash("Prestador de serviços cadastrado com sucesso", "success")
        return redirect(url_for("prestadores_servicos.listar_prestadores"))

    return render_template("prestadores_servicos/form.html")


@prestador_bp.route("/<int:prestador_id>", methods=["GET"])
def detalhar_prestador(prestador_id):
    p = PRESTADORES_DB.get(prestador_id)
    if not p:
        flash("Prestador de serviços não encontrado", "danger")
        return redirect(url_for("prestadores_servicos.listar_prestadores")), 404

    return render_template("prestadores_servicos/detalhe.html", prestador=p)


@prestador_bp.route("/<int:prestador_id>/historico-os", methods=["GET"])
def historico_ordens_servico(prestador_id):
    p = PRESTADORES_DB.get(prestador_id)
    if not p:
        flash("Prestador de serviços não encontrado", "danger")
        return redirect(url_for("prestadores_servicos.listar_prestadores")), 404

    ordens = [
        os for os in ORDENS_SERVICO_DB if os["prestador_id"] == prestador_id
    ]
    return render_template(
        "prestadores_servicos/historico_os.html",
        prestador=p,
        ordens_servico=ordens,
    )


@prestador_bp.route("/<int:prestador_id>/editar", methods=["GET", "POST"])
def editar_prestador(prestador_id):
    p = PRESTADORES_DB.get(prestador_id)
    if not p:
        flash("Prestador de serviços não encontrado", "danger")
        return redirect(url_for("prestadores_servicos.listar_prestadores")), 404

    if request.method == "POST":
        razao_social = request.form.get("razao_social", "").strip()
        cnpj = request.form.get("cnpj", "").strip()
        email = request.form.get("email", "").strip()
        telefone = request.form.get("telefone", "").strip()
        endereco = request.form.get("endereco", "").strip()

        if not (razao_social and cnpj and email and telefone and endereco):
            flash("Campos obrigatórios não preenchidos", "danger")
            return (
                render_template(
                    "prestadores_servicos/form.html", prestador=p
                ),
                400,
            )

        for outro_id, outro_p in PRESTADORES_DB.items():
            if outro_id != prestador_id and outro_p["cnpj"] == cnpj:
                flash(
                    "CNPJ já utilizado por outro prestador de serviços cadastrado",
                    "danger",
                )
                return (
                    render_template(
                        "prestadores_servicos/form.html", prestador=p
                    ),
                    400,
                )

        p["razao_social"] = razao_social
        p["cnpj"] = cnpj
        p["email"] = email
        p["telefone"] = telefone
        p["endereco"] = endereco

        flash("Dados do prestador atualizados com sucesso", "success")
        return redirect(url_for("prestadores_servicos.listar_prestadores"))

    return render_template("prestadores_servicos/form.html", prestador=p)


@prestador_bp.route("/<int:prestador_id>/editar-status", methods=["GET", "POST"])
def editar_status_prestador(prestador_id):
    p = PRESTADORES_DB.get(prestador_id)
    if not p:
        flash("Prestador de serviços não encontrado", "danger")
        return redirect(url_for("prestadores_servicos.listar_prestadores")), 404

    if request.method == "POST":
        novo_status = request.form.get("status", "").strip()

        if novo_status not in ["Ativo", "Inativo"]:
            flash("Status inválido", "danger")
            return (
                render_template(
                    "prestadores_servicos/status.html", prestador=p
                ),
                400,
            )

        p["status"] = novo_status
        p["data_alteracao_status"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        flash("Status atualizado com sucesso", "success")
        return redirect(url_for("prestadores_servicos.listar_prestadores"))

    return render_template("prestadores_servicos/status.html", prestador=p)