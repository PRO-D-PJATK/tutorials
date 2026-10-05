# 🧠 Wprowadzenie do Google Colab + Regresja Liniowa (projekt edukacyjny)

Ten projekt ma na celu pokazać Ci **jak rozpocząć pracę w Google Colab** oraz wykonać **proste zadanie z regresją liniową w Pythonie** – czyli jednym z podstawowych modeli uczenia maszynowego.

Zawiera:
- kompletny notatnik Colab (`colab_regresja.ipynb`),
- przykładowy zbiór danych (`mieszkania.csv`),
- instrukcję krok po kroku jak uruchomić i zapisać projekt na GitHubie.

---

## 🚀 1. Co to jest Google Colab?

**Google Colaboratory (Colab)** to darmowe środowisko online do pisania i uruchamiania kodu Python.  
Nie musisz nic instalować – wszystko działa w przeglądarce i zapisuje się automatycznie w Twoim **Google Drive**.

Colab pozwala:
- pisać i uruchamiać kod w języku **Python** (np. uczenie maszynowe, analizy danych, wykresy),
- zapisywać projekty w chmurze (Google Drive),
- współdzielić notatniki z innymi osobami,
- korzystać z mocy obliczeniowej Google (CPU / GPU / TPU).

---

## 🧑‍💻 2. Jak otworzyć Google Colab krok po kroku

### 🔹 Krok 1: Otwórz Google Colab z Gmaila
1. Będąc zalogowanym w Gmailu, kliknij **ikonkę 9 kropek (menu aplikacji Google)** w prawym górnym rogu.  
2. Na liście znajdź **Colab** (lub „Colaboratory”).  
3. Jeśli nie widzisz – kliknij **„Więcej z Google”** lub wpisz ręcznie w pasek przeglądarki:  
   👉 [https://colab.research.google.com](https://colab.research.google.com)

---

### 🔹 Krok 2: Otwórz notatnik z tego projektu
Masz kilka opcji:

#### ✅ Opcja A – wgraj notatnik lokalnie:
1. Rozpakuj pobrany plik ZIP z projektem.  
2. W Colab wybierz: **Plik → Prześlij notatnik (Upload notebook)**.  
3. Wskaż plik `colab_regresja.ipynb`.  
4. Gotowe — możesz uruchamiać komórki!

#### ☁️ Opcja B – zapisz kopię w Google Drive:
W Colab kliknij: **Plik → Zapisz kopię w Dysku (Save a copy in Drive)**.  
Dzięki temu Twoje zmiany będą automatycznie zapisywane w chmurze.

---

## 📊 3. Zawartość projektu

| Plik | Opis |
|------|------|
| `colab_regresja.ipynb` | Główny notatnik z kodem, instrukcjami i zadaniem |
| `mieszkania.csv` | Przykładowe dane: metraż mieszkania (m²) vs cena (tys. zł) |
| `requirements.txt` | Lista bibliotek (jeśli chcesz uruchamiać lokalnie) |
| `.gitignore` | Plik konfiguracyjny pomijający pliki tymczasowe |
| `README.md` | Ten dokument |

---

## 📚 4. Opis zadania: Regresja liniowa

### 🎯 Cel:
Przewidzieć **cenę mieszkania (w tysiącach zł)** na podstawie jego **metrażu (m²)**.

Model, którego użyjemy:  
\[
y = a \cdot x + b
\]
gdzie:
- \( y \) — przewidywana cena mieszkania,  
- \( x \) — metraż,  
- \( a \) — współczynnik nachylenia (jak szybko rośnie cena wraz z metrażem),  
- \( b \) — wyraz wolny (cena bazowa, gdy metraż = 0).

---

### 📦 Dane (`mieszkania.csv`)
| metraz_m2 | cena_tys |
|------------|-----------|
| 35 | 310 |
| 50 | 395 |
| 65 | 470 |
| 80 | 560 |
| 100 | 670 |
| 120 | 770 |

To przykładowy zbiór danych – pokazuje, że **cena rośnie wraz z metrażem**.

---

### 🔍 Krok po kroku w notatniku
W `colab_regresja.ipynb` wykonasz:

1. **Import danych** z pliku CSV (pandas).  
2. **Podział danych** na cechę (`X = metraż`) i cel (`y = cena`).  
3. **Uczenie modelu regresji liniowej** (`LinearRegression` z `scikit-learn`).  
4. **Wizualizacja wyników** na wykresie.  
5. **Predykcja** dla nowych wartości (np. 40, 60, 80 m²).

---

### 🧩 Zadania do samodzielnego wykonania

1. 💰 Dodaj kolumnę `cena_za_m2` i sprawdź, jak się zmienia wraz z metrażem.  
2. 📈 Zrób wykres: metraż (x) vs cena za m² (y).  
3. 🧮 Policz błędy modelu: średni błąd absolutny (MAE) lub średni kwadratowy (MSE).  
4. ⚙️ Spróbuj dodać drugą cechę — np. `metraz_m2 ** 2` i zobacz, czy model działa lepiej (regresja wielomianowa).  
5. 💾 Zapisz wykres do pliku PNG (`plt.savefig("regresja.png")`).

---

## 🧱 5. Struktura projektu

```

colab_regresja_projekt/
├── colab_regresja.ipynb
├── mieszkania.csv
├── requirements.txt
├── .gitignore
└── README.md

```

---

## 🌍 6. Jak opublikować projekt na GitHubie

### 🔹 Opcja 1 — przez przeglądarkę (najprostsza)
1. Wejdź na [https://github.com](https://github.com) i zaloguj się.  
2. Kliknij przycisk **New Repository**.  
3. Nazwij projekt, np. `colab-regresja`.  
4. W nowym repozytorium przeciągnij i upuść pliki z folderu projektu (`.ipynb`, `.csv`, `README.md`, itd.).  
5. Kliknij **Commit changes**.

---

### 🔹 Opcja 2 — bezpośrednio z Colab
1. W Colab wybierz: **Plik → Zapisz kopię w GitHubie**.  
2. Wybierz swoje repozytorium.  
3. Dodaj komentarz np. „Pierwsza wersja projektu regresji liniowej”.  
4. Kliknij **OK** – gotowe!

---

## 🧠 7. Wiedza w pigułce – co zapamiętać

- **Colab** to darmowe środowisko Pythona w przeglądarce.  
- **Regresja liniowa** przewiduje wartości ciągłe (np. ceny, temperatury).  
- W `scikit-learn` model tworzymy za pomocą `LinearRegression()`.  
- Warto wizualizować dane – to pomaga lepiej zrozumieć wyniki.  
- **GitHub** pozwala dzielić się kodem i tworzyć portfolio projektów.

---

## ✅ 8. Co dalej?

- Spróbuj wczytać **własny zbiór danych** (np. ceny aut, wzrost vs waga, itp.).
- Zmień model na `PolynomialFeatures` i sprawdź, jak dopasowanie się zmienia.
- Utwórz nowy notebook w Colab i poeksperymentuj!

---

## ✅ 9. Wyniki

- Stwórz repo w organizacji **PROJ-D-2024** o nazwie "Colabolatory_<numer-studenta>"
- Wyślij link do swojego repozytoiru w zadaniu na Temsach.
