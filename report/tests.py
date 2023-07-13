from report.models import RamUsage


def test_set_and_get_ram_stats():
    ram_usage_instance = RamUsage("test")
    ram_usage_instance.set_ram_stats()
    results = ram_usage_instance.get_ram_stats()
    assert len(results) == 1
    ram_usage_instance.drop_table_if_exists()
