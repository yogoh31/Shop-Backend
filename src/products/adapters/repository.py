import abc

from products.domain import model


class AbstractRepository(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def add(self, product: model.Product):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, sku: str | None = None) -> model.Product:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self._session = session

    def add(self, product):
        self._session.add(product)

    def get(self, sku=None):
        products = self._session.query(model.Product)
        if(sku):
            return products.filter_by(sku=sku).first()
        return products.all()
        # return self._session.query(model.Product).filter_by(sku=sku).first()

    # def get_order_lines(self, order_id):
    #     return self._session.query(model.OrderLine).filter_by(order_id=order_id).all()
