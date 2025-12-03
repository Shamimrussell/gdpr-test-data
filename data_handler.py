"""
GDPR-säker datahantering för testning
Syfte: Visa hur man skyddar personuppgifter i testdata
"""

import hashlib

def mask_personal_id(personal_id):
    """Maskerar personnummer - visar bara delar för felsökning"""
    if personal_id and len(personal_id) > 4:
        return personal_id[:4] + "*" * (len(personal_id) - 4)
    return personal_id

def anonymize_name(name):
    """Anonymiserar namn för testdata - skapar ofarlig data"""
    if name:
        name_hash = hashlib.md5(name.encode()).hexdigest()[:8]
        return f"Testperson_{name_hash}"
    return "Testperson_XXX"

def mask_email(email):
    """Maskerar e-post för felsökning"""
    if email and "@" in email:
        parts = email.split("@")
        if len(parts[0]) > 2:
            return parts[0][:2] + "*" * (len(parts[0])-2) + "@" + parts[1]
    return email

def create_safe_test_data():
    """Skapar GDPR-säker testdata för automatiserade tester"""
    
    # Original data (skulle vara känslig i verkligheten)
    original_customers = [
        {"name": "Anna Andersson", "personal_id": "19850101-1234", "email": "anna.andersson@example.com"},
        {"name": "Lars Larsson", "personal_id": "19780214-5678", "email": "lars.larsson@example.com"},
        {"name": "Eva Eriksson", "personal_id": "19901224-9012", "email": "eva.eriksson@example.com"},
        {"name": "Mikael Johansson", "personal_id": "19830615-4321", "email": "mikael.johansson@example.com"}
    ]
    
    # Säker testdata (anonymiserad)
    safe_test_data = []
    
    for i, customer in enumerate(original_customers, 1):
        safe_customer = {
            "name": anonymize_name(customer["name"]),
            "personal_id": mask_personal_id(customer["personal_id"]),
            "email": f"user{i}@testcompany.example"
        }
        safe_test_data.append(safe_customer)
    
    return safe_test_data

# Testa funktionerna
if __name__ == "__main__":
    print("=== GDPR TESTDATA GENERATOR ===")
    
    safe_data = create_safe_test_data()
    
    print("\n🔒 ORIGINAL DATA (KÄNSLIG - GDPR SKYDDAD):")
    print("Namn: Anna Andersson")
    print("Personnummer: 19850101-1234")
    print("E-post: anna.andersson@example.com")
    
    print("\n✅ SÄKER TESTDATA (GDPR-ANPASSAD - SAFE FÖR TEST):")
    for customer in safe_data:
        print(f"Namn: {customer['name']}")
        print(f"Personnummer: {customer['personal_id']}")
        print(f"E-post: {customer['email']}")
        print("---")