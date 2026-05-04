from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Categoria, Produto

app = FastAPI(title="Sistema de Loja")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def exibir_home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request": request}

    )

#FUNÇÕES CATEGORIA
#LISTAR
@app.get("/categorias")
def exibir_categorias(request: Request, db: Session = Depends(get_db)):
    categorias = db.query(Categoria).all()
    return templates.TemplateResponse(
        request,
        "categorias.html",
        {"request": request,
         "categorias": categorias
        }
    )

#CADASTRAR
@app.post("/categorias")
def cadastrar_categorias(
    nome: str = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    nova_categoria = Categoria(nome=nome, descricao=descricao)
    db.add(nova_categoria)
    db.commit()
    return RedirectResponse(url="/categorias", status_code=303)

#DELETAR
@app.post("/categorias/{id}/deletar")
def deletar_categoria(id: int, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter_by(id=id).first()
    if categoria:
        db.delete(categoria)
        db.commit()
    return RedirectResponse(url="/categorias", status_code=303)

#ATUALIZAR
@app.get("/categorias/{id}/editar")
def editar_categoria(id: int, request: Request, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter_by(id=id).first()
    return templates.TemplateResponse(
        request,
        "atualizar_categoria.html",
        {"request": request,
         "categoria": categoria,
        }
    )

@app.post("/categorias/{id}/editar")
def atualizar_categoria(
    id: int,
    nome: str = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    atualizao_categoria = db.query(Categoria).filter_by(id=id).first()
    if atualizao_categoria:
        atualizao_categoria.nome = nome
        atualizao_categoria.descricao = descricao
        db.commit()
    return RedirectResponse(url="/categorias", status_code=303)


#FUNÇÕES PRODUTOS
#LISTAR
@app.get("/produtos")
def exibir_produtos(request: Request, db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()
    categorias = db.query(Categoria).all()
    return templates.TemplateResponse(
        request,
        "produtos.html",
        {"request": request,
         "produtos": produtos,
         "categorias": categorias
        }
    )

#CADASTRAR
@app.post("/produtos")
def cadastrar_produtos(
    nome: str = Form(...),
    preco: float = Form(...),
    estoque: int = Form(...),
    categoria_id: int = Form(...),
    db: Session = Depends(get_db)
):
    novo_produto = Produto(
        nome=nome,
        preco=preco,
        estoque=estoque,
        categoria_id=categoria_id
    )
    db.add(novo_produto)
    db.commit()
    return RedirectResponse(url="/produtos", status_code=303)

#DELETAR
@app.post("/produtos/{id}/deletar")
def deletar_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter_by(id=id).first()
    if produto:
        db.delete(produto)
        db.commit()
    return RedirectResponse(url="/produtos", status_code=303)

# ATUALIZAR PRODUTO
@app.get("/produtos/{id}/editar")
def editar_produto(id: int, request: Request, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter_by(id=id).first()
    categorias = db.query(Categoria).all()  # Necessário para o select de categorias
    return templates.TemplateResponse(
        request,
        "atualizar_produto.html",
        {
            "request": request,
            "produto": produto,
            "categorias": categorias
        }
    )

# ATUALIZAR PRODUTO
@app.post("/produtos/{id}/editar")
def atualizar_produto(
    id: int,
    nome: str = Form(...),
    preco: float = Form(...),
    estoque: int = Form(...),
    categoria_id: int = Form(...),
    db: Session = Depends(get_db)
):
    produto_existente = db.query(Produto).filter_by(id=id).first()
    if produto_existente:
        produto_existente.nome = nome
        produto_existente.preco = preco
        produto_existente.estoque = estoque
        produto_existente.categoria_id = categoria_id
        db.commit()
    return RedirectResponse(url="/produtos", status_code=303)