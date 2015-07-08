from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet


@dataset([DataSet("tad")])
class TestTad(ArtemisTestFixture):
    """
    On demand transport tests
    """
    # Tad commune a commune
    def test_city_2_city(self):
        self.journey(_from="admin:41246",
                     to="admin:41266",
                     datetime="20150302T102000")

    def test_city_2_coord(self):
        self.journey(_from="admin:41246",
                     to="1.2391;47.4599",
                     datetime="20150302T102000")

    def test_coord_2_city(self):
        self.journey(_from="1.3347;475096",
                     to="admin:41266",
                     datetime="20150302T102000")

    def test_coord_2_coord(self):
        self.journey(_from="1.3347;475096",
                     to="1.2391;47.4599",
                     datetime="20150302T102000")

    # Tad commune a arret
    def test_stop_point_2_city(self):
        self.journey(_from="stop_point:CAA:SP:blr2",
                     to="admin:41212",
                     datetime="20150310T102000")

    def test_stop_area_2_city(self):
        self.journey(_from="stop_area:T18:SA:blr1",
                     to="admin:41212",
                     datetime="20150310T102000")

    def test_stop_point_2_coord(self):
        self.journey(_from="stop_point:CAA:SP:blr2",
                     to="1.3573;47.5564",
                     datetime="20150310T102000")

    def test_stop_area_2_coord(self):
        self.journey(_from="stop_area:T18:SA:blr1",
                     to="1.3573;47.5564",
                     datetime="20150310T102000")

    def test_city_2_stop_point(self):
        self.journey(_from="admin:41212",
                     to="stop_point:CAA:SP:blr2",
                     datetime="20150310T102000")

    def test_city_2_stop_area(self):
        self.journey(_from="admin:41212",
                     to="stop_area:T18:SA:blr1",
                     datetime="20150310T102000")

    def test_coord_2_stop_point(self):
        self.journey(_from="1.3573;47.5564",
                     to="stop_point:CAA:SP:blr2",
                     datetime="20150310T102000")

    def test_coord_2_stop_area(self):
        self.journey(_from="1.3573;47.5564",
                     to="stop_area:T18:SA:blr1",
                     datetime="20150310T102000")

    # Tad commune a arret (depart apres)
    def test_stop_point_2_city_dep_after(self):
        self.journey(_from="stop_point:CA2:SP:blr1",
                     to="admin:41295",
                     datetime="20150313T102000")

    def test_stop_area_2_city_dep_after(self):
        self.journey(_from="stop_area:CA2:SA:blr1",
                     to="admin:41295",
                     datetime="20150313T102000")

    def test_stop_point_2_coord_dep_after(self):
        self.journey(_from="stop_point:CA2:SP:blr1",
                     to="1.3828;47.5831",
                     datetime="20150313T102000")

    def test_stop_area_2_coord_dep_after(self):
        self.journey(_from="stop_area:CA2:SA:blr1",
                     to="1.3828;47.5831",
                     datetime="20150313T102000")

    def test_city_2_stop_point_dep_after(self):
        self.journey(_from="admin:41295",
                     to="stop_point:CA2:SP:blr1",
                     datetime="20150313T102000")

    def test_city_2_stop_area_dep_after(self):
        self.journey(_from="admin:41212",
                     to="stop_area:CA2:SA:blr1",
                     datetime="20150313T102000")

    def test_coord_2_stop_point_dep_after(self):
        self.journey(_from="1.3828;47.5831",
                     to="stop_point:CA2:SP:blr1",
                     datetime="20150313T102000")

    def test_coord_2_stop_area_dep_after(self):
        self.journey(_from="1.3828;47.5831",
                     to="stop_area:CA2:SA:blr1",
                     datetime="20150313T102000")

    # Tad commune a arret (arrivee avant)
    def test_stop_point_2_city_arr_before(self):
        self.journey(_from="stop_point:CA1:SP:blr9",
                     to="admin:41047",
                     datetime="20150319T102000")

    def test_stop_area_2_city_arr_before(self):
        self.journey(_from="stop_area:CA1:SA:blr9",
                     to="admin:41047",
                     datetime="20150319T102000")

    def test_stop_point_2_coord_arr_before(self):
        self.journey(_from="stop_point:CA1:SP:blr9",
                     to="1.3561;47.6089",
                     datetime="20150319T102000")

    def test_stop_area_2_coord_arr_before(self):
        self.journey(_from="stop_area:CA1:SA:blr9",
                     to="1.3561;47.6089",
                     datetime="20150319T102000")

    def test_city_2_stop_point_arr_before(self):
        self.journey(_from="admin:41047",
                     to="stop_point:CA1:SP:blr9",
                     datetime="20150319T102000")

    def test_city_2_stop_area_arr_before(self):
        self.journey(_from="admin:41047",
                     to="stop_area:CA1:SA:blr9",
                     datetime="20150319T102000")

    def test_coord_2_stop_point_arr_before(self):
        self.journey(_from="1.3561;47.6089",
                     to="stop_point:CA1:SP:blr9",
                     datetime="20150319T102000")

    def test_coord_2_stop_area_arr_before(self):
        self.journey(_from="1.3561;47.6089",
                     to="stop_area:CA1:SA:blr9",
                     datetime="20150319T102000")

    # Tad commune a arret (arrivee avant & depart apres)
    def test_stop_point_2_city_arr_dep(self):
        self.journey(_from="stop_point:CA3:SP:blr9",
                     to="admin:41295",
                     datetime="20150407T102000")

    def test_stop_area_2_city_arr_dep(self):
        self.journey(_from="stop_area:CA3:SA:blr9",
                     to="admin:41295",
                     datetime="20150407T102000")

    def test_stop_point_2_coord_arr_dep(self):
        self.journey(_from="stop_point:CA3:SP:blr9",
                     to="1.3828;47.5831",
                     datetime="20150407T102000")

    def test_stop_area_2_coord_arr_dep(self):
        self.journey(_from="stop_area:CA3:SA:blr9",
                     to="1.3828;47.5831",
                     datetime="20150407T102000")

    def test_city_2_stop_point_arr_dep(self):
        self.journey(_from="admin:41295",
                     to="stop_point:CA3:SP:blr9",
                     datetime="20150407T102000")

    def test_city_2_stop_area_arr_dep(self):
        self.journey(_from="admin:41295",
                     to="stop_area:CA3:SA:blr9",
                     datetime="20150407T102000")

    def test_coord_2_stop_point_arr_dep(self):
        self.journey(_from="1.3828;47.5831",
                     to="stop_point:CA3:SP:blr9",
                     datetime="20150407T102000")

    def test_coord_2_stop_area_arr_dep(self):
        self.journey(_from="1.3828;47.5831",
                     to="stop_area:CA3:SA:blr9",
                     datetime="20150407T102000")