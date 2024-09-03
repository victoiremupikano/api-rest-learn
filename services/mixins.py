class QSFilterWithFacture():
    def get_queryset(self, *args, **kwargs):
        facture_id=self.request.parser_context.get('kwargs').get('facture_id')
        qs=super().get_queryset(*args, **kwargs)
        return qs.filter(facture_id=facture_id)