from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for

operadora_bp = Blueprint("operadoras_energia", __name__)

OPERADORAS_DB = {
    1: {
        "id": 1,
        "cnpj": "08.823.111/0001-90",
        "razao_social": "Energisa PB Distribuidora",
        "telefone": "(83) 3218-0000",
        "email": "contato@energisa.com.br",
        "endereco": "BR 230 KM 12",
        "site": "www.energisa.com.br",
        "status": "Ativo",
        "data_alteracao_status": "2026-10-01 08:00:00",
    },
    2: {
        "id": 2,
        "cnpj": "08.823.555/0001-10",
        "razao_social": "Neoenergia Borborema",
        "telefone": "(83) 3310-2000",
        "email": "atendimento@neoenergia.com",
        "endereco": "Av. Brasil, 100",
        "site": "www.neoenergia.com",
        "status": "Inativo",
        "data_alteracao_status": "2026-09-15 11:20:00",
    },
}


@operadora_bp.route("/", methods=["GET"])
def listar_operadoras():
    termo = request.args.get("termo", "").strip().lower()
    status_filtro = request.args.get("status", "").strip()

    resultados = list(OPERADORAS_DB.values())

    if termo:
        resultados = [
            op
            for op in resultados
            if termo in op["razao_social"].lower() or termo in op["cnpj"].lower()
        ]

    if status_filtro:
        resultados = [
            op
            for op in resultados
            if op["status"].lower() == status_filtro.lower()
        ]

    return render_template("operadoras_energia/index.html", operadoras=resultados)


@operadora_bp.route("/novo", methods=["GET", "POST"])
def criar_operadora():
    if request.method == "POST":
        cnpj = request.form.get("cnpj", "").strip()
        razao_social = request.form.get("razao_social", "").strip()
        telefone = request.form.get("telefone", "").strip()
        email = request.form.get("email", "").strip()
        status = request.form.get("status", "Ativo").strip()
        endereco = request.form.get("endereco", "").strip()
        site = request.form.get("site", "").strip()

        if not (cnpj and razao_social and telefone and email and status):
            flash("Campos obrigatórios não preenchidos", "danger")
            return render_template("operadoras_energia/form.html"), 400

        for op in OPERADORAS_DB.values():
            if op["cnpj"] == cnpj:
                flash("O sistema deve impedir duplicidade de CNPJ", "danger")
                return render_template("operadoras_energia/form.html"), 400

        novo_id = (
            max(OPERADORAS_DB.keys(), default=0) + 1 if OPERADORAS_DB else 1
        )

        OPERADORAS_DB[novo_id] = {
            "id": novo_id,
            "cnpj": cnpj,
            "razao_social": razao_social,
            "telefone": telefone,
            "email": email,
            "endereco": endereco,
            "site": site,
            "status": status,
            "data_alteracao_status": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        flash("Operadora de energia cadastrada com sucesso", "success")
        return redirect(url_for("operadoras_energia.listar_operadoras"))

    return render_template("operadoras_energia/form.html")


@operadora_bp.route("/<int:op_id>", methods=["GET"])
def detalhar_operadora(op_id):
    op = OPERADORAS_DB.get(op_id)
    if not op:
        flash("Operadora de energia não encontrada", "danger")
        return redirect(url_for("operadoras_energia.listar_operadoras")), 404

    return render_template("operadoras_energia/detalhe.html", operadora=op)


@operadora_bp.route("/<int:op_id>/editar", methods=["GET", "POST"])
def editar_operadora(op_id):
    op = OPERADORAS_DB.get(op_id)
    if not op:
        flash("Operadora de energia não encontrada", "danger")
        return redirect(url_for("operadoras_energia.listar_operadoras")), 404

    if request.method == "POST":
        razao_social = request.form.get("razao_social", "").strip()
        cnpj = request.form.get("cnpj", "").strip()
        email = request.form.get("email", "").strip()
        telefone = request.form.get("telefone", "").strip()
        endereco = request.form.get("endereco", "").strip()

        if not (razao_social and cnpj and email and telefone):
            flash("Campos obrigatórios não preenchidos", "danger")
            return render_template("operadoras_energia/form.html", operadora=op), 400

        for outro_id, outro_op in OPERADORAS_DB.items():
            if outro_id != op_id and outro_op["cnpj"] == cnpj:
                flash(
                    "CNPJ já utilizado por outra operadora cadastrada", "danger"
                )
                return (
                    render_template(
                        "operadoras_energia/form.html", operadora=op
                    ),
                    400,
                )

        op["razao_social"] = razao_social
        op["cnpj"] = cnpj
        op["email"] = email
        op["telefone"] = telefone
        op["endereco"] = endereco

        flash("Dados da operadora atualizados com sucesso", "success")
        return redirect(url_for("operadoras_energia.listar_operadoras"))

    return render_template("operadoras_energia/form.html", operadora=op)


@operadora_bp.route("/<int:op_id>/editar-status", methods=["GET", "POST"])
def editar_status_operadora(op_id):
    op = OPERADORAS_DB.get(op_id)
    if not op:
        flash("Operadora de energia não encontrada", "danger")
        return redirect(url_for("operadoras_energia.listar_operadoras")), 404

    if request.method == "POST":
        novo_status = request.form.get("status", "").strip()

        if novo_status not in ["Ativo", "Inativo"]:
            flash("Status inválido", "danger")
            return render_template("operadoras_energia/status.html", operadora=op), 400

        op["status"] = novo_status
        op["data_alteracao_status"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        flash("Status atualizado com sucesso", "success")
        return redirect(url_for("operadoras_energia.listar_operadoras"))

    return render_template("operadoras_energia/status.html", operadora=op)