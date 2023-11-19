from db import Pallet, PalletStatus, Status, ApiKeys
class PaletSql:
    @staticmethod
    def get_secret_key(api_key):
        api_secret = ApiKeys.get(api_key=api_key)
        return api_secret
    @staticmethod
    def production(data):
        Pallet.create(**data)
        PalletStatus.create(id_pallet=data['id_pallet'], id_status=1)

    @staticmethod
    def get_pallet_status(id_pallet):
        pallet_status_id = PalletStatus.get(id_pallet=id_pallet).id_status
        pallet_status_name = Status.get(id_status=pallet_status_id).status_name
        return {'name_status': pallet_status_name, 'id_status': pallet_status_id}

    def information(self):
        all_pallet_data = {}
        for pallet in Pallet.select():
            id_palet = pallet.id_pallet
            pallet_status = self.get_pallet_status(id_palet).get('name_status')
            pallet_data = {
                'id_pallet': pallet.id_pallet,
                'product_name': pallet.product_name,
                'product_batch': pallet.product_batch,
                'thing_quantity': pallet.thing_quantity,
                'data_of_manufacture': pallet.data_of_manufacture,
                'expiration_date': pallet.expiration_date,
                'status_name': pallet_status,
            }
            all_pallet_data.setdefault(id_palet, pallet_data)
        return all_pallet_data

    @staticmethod
    def one_pallet(id_pallet):
        data_pallet = Pallet.get(id_pallet=id_pallet)
        id_status = PalletStatus.get(id_pallet=id_pallet).id_status
        data_status = Status.get(id_status=id_status)
        return {
            'id_pallet': data_pallet.id_pallet,
            'product_name': data_pallet.product_name,
            'product_batch': data_pallet.product_batch,
            'thing_quantity': data_pallet.thing_quantity,
            'data_of_manufacture': data_pallet.data_of_manufacture,
            'expiration_date': data_pallet.expiration_date,
            'status': data_status.status_name
        }

    def change_pallet_status(self, id_pallet):
        pallet_status_old = self.get_pallet_status(id_pallet).get('id_status')
        updated_data = PalletStatus.update(id_status=pallet_status_old+1).where(PalletStatus.id_pallet==id_pallet)
        updated_data.execute()
        return self.one_pallet(id_pallet)

if __name__ == '__main__':
    pass
