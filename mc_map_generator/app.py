from .mappers import Plotter
from .readers import FileReader


class Mapper:

    @staticmethod
    def run():
        mapper = Plotter()
        reader = FileReader()

        reader.read_csv_file('informacion_estaciones_red_calidad_aire.csv')
        station_list = reader.data

        print(station_list.head())

        locations = station_list.iloc[:, [25, 24]].values
        station_name = station_list.iloc[:, [2]].values
        mapper.add_station_marker(locations=locations, station_names=station_name)

        mapper.generate_map('test')
