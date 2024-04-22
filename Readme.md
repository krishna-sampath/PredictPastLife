# Past Life Predictor

## Dataset
The dataset utilized in this project has been generated using the 'dataset.py' script. It encompasses five main features, namely Year, Month, and Day. These features serve as inputs, while two output features, namely "Trait" and "Descriptor", categorize the data into classes. Consequently, a classification algorithm is employed for analysis.

## Model
The model employed in this project leverages the input features "Year", "Month", and "Day" to predict the classes for the features "Trait" and "Descriptor". It utilizes the Support Vector Machine (SVM) classifier with a linear kernel function to accomplish this task.

## App.py
The application utilizes Flask, a Python web framework, to render two HTML files: "index.html" and "result.html". Users input their Date of Birth (DOB), and the application provides them with the output corresponding to their trait and description in their past life.
