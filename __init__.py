# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Afectaciones_servidumbres
                                 A QGIS plugin
 Este plugin permite determinar las afectaciones prediales que conlleva un proyecto de sismica
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-05-05
        copyright            : (C) 2020 by Diana Alejandra Bocanegra
        email                : bocanegra.pataquiva.diana@usal.es
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Afectaciones_servidumbres class from file Afectaciones_servidumbres.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Servidumbres_modulo import Afectaciones_servidumbres
    return Afectaciones_servidumbres(iface)
