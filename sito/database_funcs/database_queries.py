from ..modelli import User, Classi, Cronologia


def user_da_nominativo(nominativo: str) -> User | None:
    """
    restituisce un oggetto utente dato il suo nominativo
    """
    return User.query.filter_by(nominativo=nominativo).first()


def user_da_id(id: int) -> User | None:
    """
    restituisce un oggetto utente dato il suo id
    """
    return User.query.filter_by(id=id).first()


def user_da_email(email: str) -> User | None:
    """
    restituisce un oggetto utente dato la sua email
    """
    return User.query.filter_by(email=email).first()


def studenti_da_classe(classe: Classi) -> list[User]:
    """
    restituisce gli studenti di una classe
    """
    return classe.studenti


def classe_da_nome(classe_name: str) -> Classi | None:
    """
    restituisce un oggetto classe dato il suo nome
    """
    return Classi.query.filter_by(classe=classe_name).first()


def classe_da_id(classe_id: int) -> Classi | None:
    """
    restituisce un oggetto classe dato il suo id
    """
    return Classi.query.filter_by(id=classe_id).first()
