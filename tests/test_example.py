def test_validate_page_loads(ui):
    ui.home.load_page()
    ui.home.get_started()
    ui.intro.wait_for_installation_heading()
