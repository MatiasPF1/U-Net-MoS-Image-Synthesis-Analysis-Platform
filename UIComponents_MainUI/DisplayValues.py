from dash import Input, Output, html

# This function is a transformer function, Will Handle None or Empty values and convert them to "0"
def format_value(value): 
    if value is None or value == "":
        return "0"
    return str(value)


def register_display_values_callback(app):    
    @app.callback(
        Output('values-display-content', 'children'),
        Input('mat-name', 'value'),
        Input('pixel-size', 'value'),
        Input('metal-atom', 'value'),
        Input('lattice-const', 'value'),
        Input('img-size', 'value'),
        Input('chal-atom', 'value'),
        Input('sub-atom-metal', 'value'),
        Input('metal-sub-conc', 'value'),
        Input('metal-vac-conc', 'value'),
        Input('sub-atom-chal', 'value'),
        Input('chal-sub-conc', 'value'),
        Input('vac-one-conc', 'value'),
        Input('vac-two-conc', 'value'),
        Input('sub-two-conc', 'value'),
        Input('sub-one-conc', 'value'),
        Input('voltage', 'value'),
        Input('aperture', 'value'),
        Input('defocus', 'value'),
        Input('dwell-time', 'value'),
        Input('cs3-mean', 'value'),
        Input('cs3-std', 'value'),
        Input('cs5-mean', 'value'),
        Input('cs5-std', 'value'),
        Input('adf-angle-min', 'value'),
        Input('adf-angle-max', 'value'),
        Input('src-size-mean', 'value'),
        Input('defoc-spread-mean', 'value'),
        Input('probe-cur-mean', 'value'),
        Input('src-size-std', 'value'),
        Input('defoc-spread-std', 'value'),
        Input('probe-cur-std', 'value'),
    )
    def update_values_display(mat_name, pixel_size, metal_atom, lattice_const, img_size, chal_atom,
                             sub_atom_metal, metal_sub_conc, metal_vac_conc, sub_atom_chal,
                             chal_sub_conc, vac_one_conc, vac_two_conc, sub_two_conc, sub_one_conc,
                             voltage, aperture, defocus, dwell_time,
                             cs3_mean, cs3_std, cs5_mean, cs5_std,
                             adf_angle_min, adf_angle_max,
                             src_size_mean, defoc_spread_mean, probe_cur_mean,
                             src_size_std, defoc_spread_std, probe_cur_std):
        
        # Create rows for each parameter with label and value
        rows = []
        
        # Material Properties Section
        rows.append(html.Div([html.H6("Material Properties", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Material Name: "), html.Span(format_value(mat_name), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Pixel Size: "), html.Span(format_value(pixel_size), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Metal Atom #: "), html.Span(format_value(metal_atom), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Lattice Constant: "), html.Span(format_value(lattice_const), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Image Size: "), html.Span(format_value(img_size), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Chalcogen Atom #: "), html.Span(format_value(chal_atom), className="value-text")], className="value-row"))
        
        # Metal Site Defects
        rows.append(html.Div([html.H6("Metal Site Defects", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Sub. Atom #: "), html.Span(format_value(sub_atom_metal), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Sub. Conc: "), html.Span(format_value(metal_sub_conc), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Vacancy Conc: "), html.Span(format_value(metal_vac_conc), className="value-text")], className="value-row"))
        
        # Chalcogen Site Defects
        rows.append(html.Div([html.H6("Chalcogen Site Defects", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Sub. Atom #: "), html.Span(format_value(sub_atom_chal), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Sub. Conc: "), html.Span(format_value(chal_sub_conc), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Vacancy One: "), html.Span(format_value(vac_one_conc), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Vacancy Two: "), html.Span(format_value(vac_two_conc), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Sub. Two: "), html.Span(format_value(sub_two_conc), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Sub. One: "), html.Span(format_value(sub_one_conc), className="value-text")], className="value-row"))
        
        # Microscope Settings
        rows.append(html.Div([html.H6("Microscope Settings", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Voltage: "), html.Span(format_value(voltage), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Aperture: "), html.Span(format_value(aperture), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Defocus: "), html.Span(format_value(defocus), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Dwell Time: "), html.Span(format_value(dwell_time), className="value-text")], className="value-row"))
        
        # Aberration Coefficients
        rows.append(html.Div([html.H6("Aberration Coefficients", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Cs3 Mean: "), html.Span(format_value(cs3_mean), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Cs3 Std: "), html.Span(format_value(cs3_std), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Cs5 Mean: "), html.Span(format_value(cs5_mean), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Cs5 Std: "), html.Span(format_value(cs5_std), className="value-text")], className="value-row"))
        
        # ADF Settings
        rows.append(html.Div([html.H6("ADF Settings", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Angle Min: "), html.Span(format_value(adf_angle_min), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Angle Max: "), html.Span(format_value(adf_angle_max), className="value-text")], className="value-row"))
        
        # Gaussian Parameters
        rows.append(html.Div([html.H6("Gaussian Parameters", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Src Size Mean: "), html.Span(format_value(src_size_mean), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Src Size Std: "), html.Span(format_value(src_size_std), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Defoc Spread Mean: "), html.Span(format_value(defoc_spread_mean), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Defoc Spread Std: "), html.Span(format_value(defoc_spread_std), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Probe Cur Mean: "), html.Span(format_value(probe_cur_mean), className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Probe Cur Std: "), html.Span(format_value(probe_cur_std), className="value-text")], className="value-row"))
        
        return rows
