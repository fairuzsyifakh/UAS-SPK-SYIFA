from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Handphone(Base):
    __tablename__ = "handphone"

    Brand : Mapped[str] = mapped_column(primary_key=True)
    Reputasi : Mapped[str]
    Antutu_Score : Mapped[int]
    Batery : Mapped[int]
    Harga : Mapped[int]
    Ukuran_Layar : Mapped[float]

    def __repr__(self) -> str :
        return f"Brand={self.Brand}, Reputasi={self.Reputasi}, Antutu_Score={self.Antutu_Score}, Batery={self.Batery}, Harga={self.Harga}, Ukuran_Layar={self.Ukuran_Layar}"
