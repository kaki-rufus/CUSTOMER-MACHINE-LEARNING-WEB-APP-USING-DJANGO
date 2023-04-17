from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import joblib
import zipfile
import os
import tensorflow as tf
from keras.models import load_model
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# create your models here

class Back(models.Model):
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'back'
        verbose_name_plural = 'back'


class Data(models.Model):
    # gender = models.PositiveIntegerField(choices=((1, 'Male'), (0, 'Female')), null=True)
 
    # @property
    # def gender_display(self):
    #     if self.gender == 0:
    #         return 'Female'
    #     elif self.gender == 1:
    #         return 'Male'
    #     else:
    #         return ''

    # def __str__(self):
    #     return self.gender_display

    tenure = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(72)], null=True)

    seniorCitizen = models.PositiveIntegerField(choices=((1, 'Yes'), (0, 'No')), null=True)

    @property
    def seniorCitizen_display(self):
        if self.seniorCitizen == 1:
            return 'Yes'
        elif self.seniorCitizen == 0:
            return 'No'
        else:
            return ''

    def __str__(self):
        return self.seniorCitizen_display

    partner = models.PositiveIntegerField(null=True, choices=((1, 'Yes'), (0, 'No')))

    @property
    def partner_display(self):
        if self.partner == 1:
            return 'Yes'
        elif self.partner == 0:
            return 'No'
        else:
            return ''

    def __str__(self):
        return self.partner_display

    dependents = models.PositiveIntegerField(choices=((1, 'Yes'), (0, 'No')), null=True)

    @property
    def dependents_display(self):
        if self.dependents == 1:
            return 'Yes'
        elif self.dependents == 0:
            return 'No'
        else:
            return ''

    def __str__(self):
        return self.dependents_display

    phone_service = models.PositiveIntegerField(choices=((1, 'Yes'), (0, 'No')), null=True)

    @property
    def phone_service_display(self):
        if self.phone_service == 1:
            return 'Yes'
        elif self.phone_service == 0:
            return 'No'
        else:
            return ''

    def __str__(self):
        return self.phone_service_display

    internet_service = models.PositiveIntegerField(choices=((1, 'Yes'), (0, 'No')), null=True)

    @property
    def internet_service_display(self):
        if self.internet_service == 1:
            return 'Yes'
        elif self.internet_service == 0:
            return 'No'
        else:
            return ''

    def __str__(self):
        return self.internet_service_display

    charges = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(8000)], decimal_places=2, max_digits=6, null=True)


    CHOICES = (
        ('Month-to-month', 'Month-to-month'), 
        ('One year', 'One year'), 
        ('Two year', 'Two year')
    )

    contract = models.CharField(max_length=30, choices=CHOICES, null=True)

    CHOICES = (
        ('Electronic check', 'Electronic check'), 
        ('Mailed check', 'Mailed check'), 
        ('Bank transfer (automatic)', 'Bank transfer (automatic)'), 
        ('Credit card (automatic)', 'Credit card (automatic)')
    )

    payment_method = models.CharField(max_length=30, choices=CHOICES, null=True)
    # date = models.DateTimeField(auto_now_add=True)
    predictions = models.CharField(max_length=20, blank=True)




    def save(self, *args, **kwargs):
        model = load_model('final_model3.h5')

        # One-hot encode the categorical variables
        cat_vars = ['contract', 'payment_method']
        encoder = OneHotEncoder(sparse=False)
        cat_data = encoder.fit_transform(np.array([[self.contract, self.payment_method]]))

        X = np.array([self.tenure, self.seniorCitizen, 
        self.partner, self.dependents, self.phone_service, self.internet_service, self.charges]).astype(np.float32)

        # Combine the encoded categorical variables with the other numerical variables
        X = np.concatenate((X, cat_data[0]), axis=None)

        X = np.expand_dims(X, axis=1)
        X = np.repeat(X, 37, axis=1)
        proba = model.predict(X)
        self.predictions = ["yes" if p > 0.5 else "no" for p in proba[0]]
        return super().save(*args, **kwargs)


    class Meta:
        # ordering = ['date']
        verbose_name = 'data'
        verbose_name_plural = 'data'











