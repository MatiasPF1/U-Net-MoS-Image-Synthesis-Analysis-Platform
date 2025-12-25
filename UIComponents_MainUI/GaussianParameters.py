from dash import html, dcc
'''
Second Part, Part 4
'''

def Gaussian_Parameters():
    return html.Div(
        [
            html.H4("Gaussian Parameters", className="section-title"),
            html.P("Configure Gaussian parameters for STEM image generation(plis do not input 3e-....., explicitly input the decimals)", className="section-subtitle"),

            html.Div(
                [
                    # Column 1
                    html.Div(
                        [
                            html.Label("Source Size Mean(nm)"),
                            dcc.Input(
                                id="src-size-mean",
                                type="number",
                                className="input-field"
                            ),

                            html.Label("Defocus Spread Mean(A)"),
                            dcc.Input(
                                id="defoc-spread-mean",
                                type="number",
                                className="input-field"
                            ),

                            html.Label("Probe Current Mean(A)"),
                            dcc.Input(
                                id="probe-cur-mean",
                                type="number",
                                className="input-field"
                            ),
                        ],
                        className="form-col"
                    ),

                    # Column 2
                    html.Div(
                        [
                            html.Label("Source Size Std(nm)"),
                            dcc.Input(
                                id="src-size-std",
                                type="number",
                                className="input-field"
                            ),

                            html.Label("Defocus Spread Stf(A)"),
                            dcc.Input(
                                id="defoc-spread-std",
                                type="number",
                                className="input-field"
                            ),

                             html.Label("Probe Current Std(A)"),
                            dcc.Input(
                                id="probe-cur-std",
                                type="number",
                                className="input-field"
                            ),
                        ],
                        className="form-col"
                    )
                ],
                className="form-grid"
            )
        ],
        id="Gausian_Panel",
        className="Gausian_Panel"
    )
