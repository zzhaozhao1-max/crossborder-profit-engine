class TokenManager:
    def save_token(self, platform, store_id, token):
        return {'platform':platform,'store_id':store_id,'status':'saved'}

    def get_token(self, platform, store_id):
        return None
