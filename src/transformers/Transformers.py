from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder
from typing import List
from pandas  import DataFrame,concat
import pandas as pd
import numpy as np
class EnCoder(BaseEstimator,TransformerMixin):
    def __init__(self,OrdinalCols: List[str]=None,OrdinalCategories:List[List[str]]=None,OheCols:List[str]=None):
        self.OrdinalCols = OrdinalCols
        self.OrdinalCategories = OrdinalCategories
        self.OheCols = OheCols
        self.oe = OrdinalEncoder(categories=self.OrdinalCategories,dtype=int)
        self.ohe = OneHotEncoder(drop="if_binary",sparse_output=False,handle_unknown='ignore',dtype=int)
    def fit(self,X:DataFrame,y=None):
        check_is_fitted(self, "is_fitted_")
        X = X.copy()
        if self.OrdinalCols:
            self.oe.fit(X[self.OrdinalCols])
        if self.OheCols:
            self.ohe.fit(X[self.OheCols])
        self.is_fitted_=True
        return self
    def transform(self,X:DataFrame):
        X=X.copy().reset_index(drop=True)
        if self.OrdinalCols:
            X[self.OrdinalCols]=self.oe.transform(X[self.OrdinalCols])
        if self.OheCols:
            out = self.ohe.transform(X[self.OheCols])
            newdf = DataFrame(data=out,columns=self.ohe.get_feature_names_out(self.OheCols))
            X = X.drop(self.OheCols,axis=1)
            X = concat([X,newdf],axis=1)
        return X


class CatGroupModeImputer(BaseEstimator, TransformerMixin):

    def __init__(self, group_cols, target_col):
        self.group_cols = group_cols
        self.target_col = target_col

    def fit(self, X: DataFrame, y=None):
        self.group_modes_ = (
            X.groupby(self.group_cols)[self.target_col]
            .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
        )
        return self

    def transform(self, X: DataFrame):
        X = X.copy()

        keys = X[self.group_cols].apply(tuple, axis=1)

        X[self.target_col] = X[self.target_col].fillna(
            keys.map(self.group_modes_)
        )

        return X


class NumGroupMeanImputer(BaseEstimator, TransformerMixin):

    def __init__(self, group_cols, target_col):
        self.group_cols = group_cols
        self.target_col = target_col

    def fit(self, X: DataFrame, y=None):
        self.group_means_ = X.groupby(self.group_cols)[self.target_col].mean()
        return self

    def transform(self, X: DataFrame):
        X = X.copy()

        keys = X[self.group_cols].apply(tuple, axis=1)

        X[self.target_col] = X[self.target_col].fillna(
            keys.map(self.group_means_)
        )

        return X

class DTIImputer(BaseEstimator, TransformerMixin):

    def __init__(self,
                loan_amount_col='loan_amount',
                rate_col='rate_of_interest',
                term_col='term',
                income_col='income',
                target_col='dtir1'):

        self.loan_amount_col = loan_amount_col
        self.rate_col = rate_col
        self.term_col = term_col
        self.income_col = income_col
        self.target_col = target_col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        P = X[self.loan_amount_col]
        r = X[self.rate_col] / (12 * 100)
        n = X[self.term_col]

        emi = (P * r * (1 + r)**n) / ((1 + r)**n - 1)

        X[self.target_col] = X[self.target_col].fillna(
            emi / X[self.income_col]
        )

        return X

class LogTransform(BaseEstimator,TransformerMixin):
    def __init__(self,cols:List[str]):
        self.cols = cols
    def fit(self,X: DataFrame,y=None):
        self.is_fitted_=True
        return self
    def transform(self,X: DataFrame):
        X = X.copy()
        X[self.cols] = np.log1p(X[self.cols])