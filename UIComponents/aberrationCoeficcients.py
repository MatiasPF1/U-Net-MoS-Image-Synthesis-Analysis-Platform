from dash import html, dcc



'''
Second Part, Part 2

'''
def Abberation_Coeficients():
    return html.Div(
        [
            html.H4("Aberration Coeficients", className="section-title"),
            html.P("Mean and Standard Deviation for Cs3 and Cs5", className="section-subtitle"),

            html.Div(
                [
                    # Column 1
                    html.Div(
                        [
                            html.Label("Cs3 Mean(μm)"),
                            dcc.Input(
                                id="Cs3_Mean",
                                type="text",
                                value=300,
                                className="input-field"
                            ),

                            html.Label("Cs3 Std(μm)"),
                            dcc.Input(
                                id="Cs3_Std",
                                type="number",
                                value=75,
                                className="input-field"
                            ),
                        ],
                        className="form-col"
                    ),

                    # Column 2
                    html.Div(
                        [
                            html.Label("Cs5 Mean(mm)"),
                            dcc.Input(
                                id="Cs5_Mean",
                                type="number",
                                value=25,
                                className="input-field"
                            ),

                            html.Label("Cs5 Std(μm)"),
                            dcc.Input(
                                id="Cs5_Std",
                                type="number",
                                value=1,
                                className="input-field"
                            ),
                        ],
                        className="form-col"
                    )
                ],
                className="form-grid"
            )
        ],
        id="aberration-panel",
        className="aberration-panel"
    )
