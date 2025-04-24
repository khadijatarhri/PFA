# myapp/presidio_service.py
from presidio_analyzer import AnalyzerEngine
from presidio_analyzer import RecognizerResult
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()



def anonymize_text(text: str, entities_to_anonymize: list):
    results = analyzer.analyze(text=text, language='en')
    filtered_results = [res for res in results if res.entity_type in entities_to_anonymize]
    anonymized_result = anonymizer.anonymize(text=text, analyzer_results=filtered_results)
    return anonymized_result.text




def detect_sensitive_data(text: str):
    """
    Fonction pour détecter les données sensibles dans un texte.
    :param text: Texte à analyser.
    :return: Liste des résultats de reconnaissance des données sensibles.
    """
    results = analyzer.analyze(text=text, language='en')  # Utilisation de l'anglais ici
    return results
