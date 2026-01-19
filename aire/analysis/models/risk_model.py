"""Risk Assessment Model."""

from typing import List, Dict, Any

import pandas as pd

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

class RiskModel:
    """Machine learning model for risk assessment."""

    def __init__(self):
        self.model = RandomForestRegressor(random_state=42)
        self.label_encoder = LabelEncoder()
        self.trained = False

    def assess_risks(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Assess risks using the trained model."""
        df = pd.DataFrame(data)
        if df.empty:
            return []

        # Prepare features
        features = df[['severity', 'description_length', 'title_length']].copy()
        features['category_encoded'] = self.label_encoder.fit_transform(df['category'])

        # If enough data, train the model
        if len(df) > 5:
            X = features
            y = df['severity']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            self.model.fit(X_train, y_train)
            predictions = self.model.predict(X)
            self.trained = True
        else:
            predictions = df['severity'].values  # Fallback to original severity

        df['predicted_risk'] = predictions
        return df.to_dict('records')