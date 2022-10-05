from recipe_scrapers.reishunger import Reishunger
from tests import ScraperTest


class TestReishungerScraper(ScraperTest):
    scraper_class = Reishunger

    @property
    def test_file_name(self):
        return "{}_2".format(self.scraper_class.__name__.lower())

    def test_host(self):
        self.assertEqual("reishunger.de", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("snackicat", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Süßkartoffel-Kichererbsen-Curry", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("3 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn.reishunger.com/img7830bearbeitetklein.jpg?quality=85",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "240g Basmati Reis Pusa",
                "1 TL Kokosöl",
                "1 Dose Bio Kichererbsen",
                "200ml Kokosmilch",
                "1 Zwiebel",
                "1 Knoblauchzehe",
                "1 mittelgroße Süßkartoffel (hier: 300g)",
                "1 Paprika",
                "150ml Wasser",
                "20g Ingwer",
                "3 TL Curry",
                "Salz, Cayenne Pfeffer, Paprika edelsüß",
                "Kräuter nach Belieben (hier: Petersilie)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "1. Schritt",
                    "Zubereitung im\nKochtopf\nReis waschen. Den Reis mit kaltem Wasser bedecken. Mit den Händen den Reis in kreisenden Bewegungen waschen. Durch die überschüssige Stärke wird das Wasser trüb. Nun das Wasser abgießen und den Vorgang wiederholen bis das Wasser klar bleibt.\nReis in einen Kochtopf geben.\nWasser dazugeben. Nach Belieben salzen.\nReis 10 Minuten einweichen lassen.\nHerd auf die höchste Hitzestufe stellen und Reis aufkochen lassen.\nSobald das Wasser kocht, den Herd auf die mittlere Hitzestufe stellen und den Reis ca. 15 Minuten bei geschlossenem Deckel köcheln lassen bis das Wasser komplett aufgesogen wurde.\nNach Belieben ein Stück Butter hinzufügen.",
                    "2. Schritt",
                    "Zwiebeln und Knoblauch klein schneiden und in Kokosöl in einer Pfanne kurz anbraten.",
                    "3. Schritt",
                    "Kokosmilch und Wasser vorsichtig in die Pfanne schütten.",
                    "4. Schritt",
                    "Süßkartoffel und Paprika klein schneiden und in die Pfanne geben.",
                    "5. Schritt",
                    "Kichererbsen abtropfen, Ingwer schälen und kleinschneiden, ebenfalls in die Pfanne geben.",
                    "6. Schritt",
                    "Curry und Salz hinzugeben und bei geschlossenem Deckel kurz zum Kochen bringen, dann auf leichter Stufe circa 10 Minuten köcheln lassen.",
                    "7. Schritt",
                    "Paprika edelsüß und Cayennepfeffer hinzugeben, verrühren und ca. weitere 5 Minuten köcheln lassen, bis die Soße schön eingekocht ist.",
                    "8. Schritt",
                    "Mit Reis und Kräutern servieren, fertig. Guten Reishunger!",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4, self.harvester_class.ratings())
