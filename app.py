"""
GDPR Testdata App - Huvudapplikation
Syfte: Visa olika sätt att hantera testdata säkert
"""

from data_handler import create_safe_test_data, mask_personal_id, anonymize_name
import csv
import os

def create_test_files():
    """Skapar testfiler med både original och säker data"""
    
    # Original data (skulle vara känslig i verkligheten)
    original_data = [
        {"name": "Anna Andersson", "personal_id": "19850101-1234", "email": "anna.andersson@example.com", "diagnosis": "Diabetes"},
        {"name": "Lars Larsson", "personal_id": "19780214-5678", "email": "lars.larsson@example.com", "diagnosis": "Hjärtsjukdom"},
        {"name": "Eva Eriksson", "personal_id": "19901224-9012", "email": "eva.eriksson@example.com", "diagnosis": "Astma"}
    ]
    
    # Skapa test_data mapp om den inte finns
    if not os.path.exists("test_data"):
        os.makedirs("test_data")
    
    # Skapa original_data.csv (simulerar krypterad data)
    with open('test_data/original_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'personal_id', 'email', 'diagnosis', 'status'])
        for customer in original_data:
            writer.writerow([
                customer['name'],
                customer['personal_id'],
                customer['email'],
                customer['diagnosis'],
                '🔒 KRYPTERAD'
            ])
    
    # Skapa safe_data.csv (anonymiserad data för testning)
    safe_data = create_safe_test_data()
    with open('test_data/safe_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'personal_id', 'email', 'diagnosis', 'status'])
        for customer in safe_data:
            writer.writerow([
                customer['name'],
                customer['personal_id'],
                customer['email'],
                'Testdiagnos',  # Anonymiserad diagnos
                '✅ SÄKER FÖR TEST'
            ])
    
    print("✅ Testfiler skapade i mappen 'test_data/'")

def show_data_comparison():
    """Visar jämförelse mellan original och säker data"""
    
    print("\n" + "="*50)
    print("📊 GDPR DATAJÄMFÖRELSE")
    print("="*50)
    
    print("\n🔒 ORIGINALDATA (KÄNSLIG - SKYDDAS ENLIGT GDPR):")
    try:
        with open('test_data/original_data.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("Kör först 'create_test_files()' för att skapa filerna")
    
    print("\n✅ SÄKER TESTDATA (ANONYMISERAD - SAFE FÖR TESTNING):")
    try:
        with open('test_data/safe_data.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("Kör först 'create_test_files()' för att skapa filerna")

def main():
    """Huvudmeny för applikationen"""
    
    while True:
        print("\n" + "="*50)
        print("🏥 GDPR TESTDATA HANTERARE")
        print("="*50)
        print("1. Skapa testfiler")
        print("2. Visa datajämförelse")
        print("3. Testa enskilda funktioner")
        print("4. Avsluta")
        
        val = input("\nVälj alternativ (1-4): ")
        
        if val == "1":
            create_test_files()
        elif val == "2":
            show_data_comparison()
        elif val == "3":
            print("\n🧪 TESTA ENSKILDA FUNKTIONER:")
            print(f"Maskera personnummer: {mask_personal_id('19850101-1234')}")
            print(f"Anonymisera namn: {anonymize_name('Anna Andersson')}")
        elif val == "4":
            print("👋 Avslutar programmet...")
            break
        else:
            print("❌ Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()