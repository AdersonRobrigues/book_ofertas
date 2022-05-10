from django.db import models


class BookCompra(models.Model):
    TPENERGIA_CHOICE = (
        ('conv', 'CONV'),
        ('i5', 'I5'),
        ('i1', 'I1'),
        ('i0', 'I0'),
        ('cq5', 'CQ5'),
    )

    PROINI_CHOICE = (
        ('jan', 'JAN'),
        ('fev', 'FEV'),
        ('mar', 'MAR'),
        ('abr', 'ABR'),
        ('mai', 'MAI'),
        ('jun', 'JUN'),
        ('jul', 'JUL'),
        ('ago', 'AGO'),
        ('set', 'SET'),
        ('out', 'OUT'),
        ('nov', 'NOV'),
        ('dez', 'DEZ'),
    )

    PROFIM_CHOICE = (
        ('jan', 'JAN'),
        ('fev', 'FEV'),
        ('mar', 'MAR'),
        ('abr', 'ABR'),
        ('mai', 'MAI'),
        ('jun', 'JUN'),
        ('jul', 'JUL'),
        ('ago', 'AGO'),
        ('set', 'SET'),
        ('out', 'OUT'),
        ('nov', 'NOV'),
        ('dez', 'DEZ'),
    )
    SUB_CHOICE = (
        ('se', 'SE'),
        ('su', 'SU'),
        ('ne', 'NE'),
        ('no', 'NO'),
    )

    OPERADOR_CHOICE = (
        ('Raul', 'RAUL'),
        ('Isabella', 'ISABELLA'),
        ('Eduardo', 'EDUARDO'),
        ('Aderson', 'ADERSON'),
    )

    TP_PRECO_CHOICE = (
        ('Fixo', 'FIXO'),
        ('Pld', 'PLD'),
    )     

    Operador = models.CharField(max_length=50, choices=OPERADOR_CHOICE)
    tp_energia = models.CharField(max_length=5, choices=TPENERGIA_CHOICE)
    prod_ini = models.CharField(max_length=5, choices=PROINI_CHOICE)
    prod_fim = models.CharField(max_length=5, choices=PROFIM_CHOICE)
    volume = models.DecimalField(max_digits=6, decimal_places=3)
    tp_preco = models.CharField(max_length=5, choices=TP_PRECO_CHOICE, blank=True, null=True)
    preco = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Preço")
    submer = models.CharField(max_length=2, choices=SUB_CHOICE)
    checked = models.BooleanField("Checked",default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tp_energia


class BookVenda(models.Model):
    TPENERGIA_CHOICE = (
        ('conv', 'CONV'),
        ('i5', 'I5'),
        ('i1', 'I1'),
        ('i0', 'I0'),
        ('cq5', 'CQ5'),
    )

    PROINI_CHOICE = (
        ('jan', 'JAN'),
        ('fev', 'FEV'),
        ('mar', 'MAR'),
        ('abr', 'ABR'),
        ('mai', 'MAI'),
        ('jun', 'JUN'),
        ('jul', 'JUL'),
        ('ago', 'AGO'),
        ('set', 'SET'),
        ('out', 'OUT'),
        ('nov', 'NOV'),
        ('dez', 'DEZ'),
    )

    PROFIM_CHOICE = (
        ('jan', 'JAN'),
        ('fev', 'FEV'),
        ('mar', 'MAR'),
        ('abr', 'ABR'),
        ('mai', 'MAI'),
        ('jun', 'JUN'),
        ('jul', 'JUL'),
        ('ago', 'AGO'),
        ('set', 'SET'),
        ('out', 'OUT'),
        ('nov', 'NOV'),
        ('dez', 'DEZ'),
    )
    SUB_CHOICE = (
        ('se', 'SE'),
        ('su', 'SU'),
        ('ne', 'NE'),
        ('no', 'NO'),
    )

    OPERADOR_CHOICE = (
        ('Raul', 'RAUL'),
        ('Isabella', 'ISABELLA'),
        ('Eduardo', 'EDUARDO'),
        ('Aderson', 'ADERSON'),
    )

    TP_PRECO_CHOICE = (
        ('Fixo', 'FIXO'),
        ('Pld', 'PLD'),
    )   

    Operador = models.CharField(max_length=50, choices=OPERADOR_CHOICE)
    tp_energia = models.CharField(max_length=5, choices=TPENERGIA_CHOICE)
    prod_ini = models.CharField(max_length=5, choices=PROINI_CHOICE)
    prod_fim = models.CharField(max_length=5, choices=PROFIM_CHOICE)
    volume = models.DecimalField(max_digits=6, decimal_places=3)
    tp_preco = models.CharField(max_length=5, choices=TP_PRECO_CHOICE, blank=True, null=True)
    preco = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Preço")
    submer = models.CharField(max_length=2, choices=SUB_CHOICE)
    checked = models.BooleanField("Checked",default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tp_energia


class BookCompraMerc(models.Model):
    TPENERGIA_CHOICE = (
        ('conv', 'CONV'),
        ('i5', 'I5'),
        ('i1', 'I1'),
        ('i0', 'I0'),
        ('cq5', 'CQ5'),
    )

    PROINI_CHOICE = (
        ('jan', 'JAN'),
        ('fev', 'FEV'),
        ('mar', 'MAR'),
        ('abr', 'ABR'),
        ('mai', 'MAI'),
        ('jun', 'JUN'),
        ('jul', 'JUL'),
        ('ago', 'AGO'),
        ('set', 'SET'),
        ('out', 'OUT'),
        ('nov', 'NOV'),
        ('dez', 'DEZ'),
    )

    PROFIM_CHOICE = (
        ('jan', 'JAN'),
        ('fev', 'FEV'),
        ('mar', 'MAR'),
        ('abr', 'ABR'),
        ('mai', 'MAI'),
        ('jun', 'JUN'),
        ('jul', 'JUL'),
        ('ago', 'AGO'),
        ('set', 'SET'),
        ('out', 'OUT'),
        ('nov', 'NOV'),
        ('dez', 'DEZ'),
    )
    SUB_CHOICE = (
        ('se', 'SE'),
        ('su', 'SU'),
        ('ne', 'NE'),
        ('no', 'NO'),
    )

    OPERADOR_CHOICE = (
        ('Raul', 'RAUL'),
        ('Isabella', 'ISABELLA'),
        ('Eduardo', 'EDUARDO'),
        ('Aderson', 'ADERSON'),
    ) 

    TP_PRECO_CHOICE = (
        ('Fixo', 'FIXO'),
        ('Pld', 'PLD'),
    )   

    Operador = models.CharField(max_length=50, choices=OPERADOR_CHOICE)
    tp_energia = models.CharField(max_length=5, choices=TPENERGIA_CHOICE)
    prod_ini = models.CharField(max_length=5, choices=PROINI_CHOICE)
    prod_fim = models.CharField(max_length=5, choices=PROFIM_CHOICE)
    agente = models.CharField(max_length=50)
    volume = models.DecimalField(max_digits=6, decimal_places=3)
    tp_preco = models.CharField(max_length=5, choices=TP_PRECO_CHOICE, blank=True, null=True)
    preco = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Preço")
    submer = models.CharField(max_length=2, choices=SUB_CHOICE)
    checked = models.BooleanField("Checked",default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tp_energia


class BookVendaMerc(models.Model):
    TPENERGIA_CHOICE = (
        ('conv', 'CONV'),
        ('i5', 'I5'),
        ('i1', 'I1'),
        ('i0', 'I0'),
        ('cq5', 'CQ5'),
    )

    PROINI_CHOICE = (
        ('jan', 'JAN'),
        ('fev', 'FEV'),
        ('mar', 'MAR'),
        ('abr', 'ABR'),
        ('mai', 'MAI'),
        ('jun', 'JUN'),
        ('jul', 'JUL'),
        ('ago', 'AGO'),
        ('set', 'SET'),
        ('out', 'OUT'),
        ('nov', 'NOV'),
        ('dez', 'DEZ'),
    )

    PROFIM_CHOICE = (
        ('jan', 'JAN'),
        ('fev', 'FEV'),
        ('mar', 'MAR'),
        ('abr', 'ABR'),
        ('mai', 'MAI'),
        ('jun', 'JUN'),
        ('jul', 'JUL'),
        ('ago', 'AGO'),
        ('set', 'SET'),
        ('out', 'OUT'),
        ('nov', 'NOV'),
        ('dez', 'DEZ'),
    )
    SUB_CHOICE = (
        ('se', 'SE'),
        ('su', 'SU'),
        ('ne', 'NE'),
        ('no', 'NO'),
    )

    OPERADOR_CHOICE = (
        ('Raul', 'RAUL'),
        ('Isabella', 'ISABELLA'),
        ('Eduardo', 'EDUARDO'),
        ('Aderson', 'ADERSON'),
    ) 

    TP_PRECO_CHOICE = (
        ('Fixo', 'FIXO'),
        ('Pld', 'PLD'),
    )   

    Operador = models.CharField(max_length=50, choices=OPERADOR_CHOICE)
    tp_energia = models.CharField(max_length=5, choices=TPENERGIA_CHOICE)
    prod_ini = models.CharField(max_length=5, choices=PROINI_CHOICE)
    prod_fim = models.CharField(max_length=5, choices=PROFIM_CHOICE)
    agente = models.CharField(max_length=50)
    volume = models.DecimalField(max_digits=6, decimal_places=3)
    tp_preco = models.CharField(max_length=5, choices=TP_PRECO_CHOICE, blank=True, null=True)
    preco = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Preço")
    submer = models.CharField(max_length=2, choices=SUB_CHOICE)
    checked = models.BooleanField("Checked",default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tp_energia
