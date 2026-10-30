from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for

uc_bp = Blueprint("unidades_consumidoras", __name__)

# Simuladores de banco de dados em memória para testes e prototipação
COOPERADOS_DB = {
    1: {"id": 1, "nome": "Walmeran Trindade", "status": "Ativo"},
    2: {"id": 2, "nome": "Nadja Nóbrega", "status": "Ativo"},
    3: {"id": 3, "nome": "Carlos Eduardo", "status": "Inativo"},
}

UNIDADES_CONSUMIDORAS_DB = {
    1: {
        "id": 1,
        "codigo_conta": "UC-100239",
        "nome": "UC Sede Centro",
        "endereco": "Rua das Trincheiras, 156",
        "cooperado_id": 1,
        "cooperado_nome": "Walmeran Trindade",
        "status": "Ativo",
        "ultima_atualizacao": "2026-10-18 10:00:00",
        "usuario_atualizacao": "sistema",
    },
    2: {
        "id": 2,
        "codigo_conta": "UC-200400",
        "nome": "UC Sul - 2004",
        "endereco": "Rua Ivete de Oliveira Cardoso, 18",
        "cooperado_id": 2,
        "cooperado_nome": "Nadja Nóbrega",
        "status": "Inativo",
        "ultima_atualizacao": "2026-10-19 14:30:00",
        "usuario_atualizacao": "jairo_gestor",
    },
}


@uc_bp.route("/", methods=["GET"])
def listar_ucs():
    termo = request.args.get("termo", "").strip().lower()
    cooperado_id = request.args.get("cooperado_id", type=int)
    status_filtro = request.args.get("status", "").strip()

    resultados = list(UNIDADES_CONSUMIDORAS_DB.values())

    if termo:
        resultados = [
            uc
            for uc in resultados
            if termo in uc["nome"].lower()
            or termo in uc["endereco"].lower()
            or termo in uc["codigo_conta"].lower()
        ]

    if cooperado_id:
        resultados = [
            uc for uc in resultados if uc["cooperado_id"] == cooperado_id
        ]

    if status_filtro:
        resultados = [
            uc
            for uc in resultados
            if uc["status"].lower() == status_filtro.lower()
        ]

    return render_template(
        "unidades_consumidoras/index.html",
        unidades=resultados,
        cooperados=COOPERADOS_DB.values(),
    )


@uc_bp.route("/novo", methods=["GET", "POST"])
def criar_uc():
    if request.method == "POST":
        codigo_conta = request.form.get("codigo_conta", "").strip()
        nome = request.form.get("nome", "").strip()
        endereco = request.form.get("endereco", "").strip()
        cooperado_id = request.form.get("cooperado_id", type=int)
        status = request.form.get("status", "Ativo").strip()

        if not (codigo_conta and nome and endereco and cooperado_id):
            flash("Campos obrigatórios não preenchidos", "danger")
            return (
                render_template(
                    "unidades_consumidoras/form.html",
                    cooperados=COOPERADOS_DB.values(),
                ),
                400,
            )

        cooperado = COOPERADOS_DB.get(cooperado_id)
        if not cooperado or cooperado["status"] != "Ativo":
            flash("O cooperado selecionado precisa estar ativo", "danger")
            return (
                render_template(
                    "unidades_consumidoras/form.html",
                    cooperados=COOPERADOS_DB.values(),
                ),
                400,
            )

        novo_id = (
            max(UNIDADES_CONSUMIDORAS_DB.keys(), default=0) + 1
            if UNIDADES_CONSUMIDORAS_DB
            else 1
        )
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        UNIDADES_CONSUMIDORAS_DB[novo_id] = {
            "id": novo_id,
            "codigo_conta": codigo_conta,
            "nome": nome,
            "endereco": endereco,
            "cooperado_id": cooperado_id,
            "cooperado_nome": cooperado["nome"],
            "status": status,
            "ultima_atualizacao": data_atual,
            "usuario_atualizacao": "usuario_logado",
        }

        flash("Unidade consumidora cadastrada com sucesso", "success")
        return redirect(url_for("unidades_consumidoras.listar_ucs"))

    return render_template(
        "unidades_consumidoras/form.html", cooperados=COOPERADOS_DB.values()
    )


@uc_bp.route("/<int:uc_id>", methods=["GET"])
def detalhar_uc(uc_id):
    uc = UNIDADES_CONSUMIDORAS_DB.get(uc_id)
    if not uc:
        flash("Unidade consumidora não encontrada", "danger")
        return redirect(url_for("unidades_consumidoras.listar_ucs")), 404

    return render_template("unidades_consumidoras/detalhe.html", uc=uc)


@uc_bp.route("/<int:uc_id>/editar", methods=["GET", "POST"])
def editar_uc(uc_id):
    uc = UNIDADES_CONSUMIDORAS_DB.get(uc_id)
    if not uc:
        flash("Unidade consumidora não encontrada", "danger")
        return redirect(url_for("unidades_consumidoras.listar_ucs")), 404

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        endereco = request.form.get("endereco", "").strip()
        cooperado_id = request.form.get("cooperado_id", type=int)

        if not (nome and endereco and cooperado_id):
            flash("Campos obrigatórios não preenchidos", "danger")
            return (
                render_template(
                    "unidades_consumidoras/form.html",
                    uc=uc,
                    cooperados=COOPERADOS_DB.values(),
                ),
                400,
            )

        cooperado = COOPERADOS_DB.get(cooperado_id)
        if not cooperado or cooperado["status"] != "Ativo":
            flash(
                "O sistema deve impedir a associação com cooperados que estejam com status inativo",
                "danger",
            )
            return (
                render_template(
                    "unidades_consumidoras/form.html",
                    uc=uc,
                    cooperados=COOPERADOS_DB.values(),
                ),
                400,
            )

        uc["nome"] = nome
        uc["endereco"] = endereco
        uc["cooperado_id"] = cooperado_id
        uc["cooperado_nome"] = cooperado["nome"]
        uc["ultima_atualizacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        uc["usuario_atualizacao"] = "jairo_gestor"

        flash(
            f"Dados da unidade consumidora {nome} atualizados com sucesso",
            "success",
        )
        return redirect(url_for("unidades_consumidoras.listar_ucs"))

    return render_template(
        "unidades_consumidoras/form.html",
        uc=uc,
        cooperados=COOPERADOS_DB.values(),
    )


@uc_bp.route("/<int:uc_id>/editar-status", methods=["GET", "POST"])
def editar_status_uc(uc_id):
    uc = UNIDADES_CONSUMIDORAS_DB.get(uc_id)
    if not uc:
        flash("Unidade consumidora não encontrada", "danger")
        return redirect(url_for("unidades_consumidoras.listar_ucs")), 404

    if request.method == "POST":
        novo_status = request.form.get("status", "").strip()

        if novo_status not in ["Ativo", "Inativo"]:
            flash("Status inválido", "danger")
            return (
                render_template(
                    "unidades_consumidoras/status.html", uc=uc
                ),
                400,
            )

        uc["status"] = novo_status
        uc["ultima_atualizacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        uc["usuario_atualizacao"] = "usuario_logado"

        flash("Status da unidade consumidora atualizado com sucesso", "success")
        return redirect(url_for("unidades_consumidoras.listar_ucs"))

    return render_template("unidades_consumidoras/status.html", uc=uc)