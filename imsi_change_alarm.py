from pyvis.network import Network


class IMSI(Network):
    def __init__(self,
                 height="100%",
                 width="100%",
                 directed=True,
                 notebook=False,
                 bgcolor="#ffffff",
                 font_color=False,
                 layout=None,
                 heading="IMSI ALARM CHANGED"):

        super().__init__(
            height=height,
            width=width,
            directed=directed,
            notebook=notebook,
            bgcolor=bgcolor,
            font_color=font_color,
            layout=layout,
            heading=heading
        )
        self._generate_node()
        self._add_edges()

    def _generate_node(self):
        self.add_node("START", label="Start", shape="ellipse", color="green")
        self.add_node("IMSI_CHANGED_ALARM",
                      label="IMSI change alarm triggered", shape="diamond")
        self.add_node(
            "IS_IMSI_CHANGED", label='IMSI change for same MSISDN Observed', shape="diamond")
        self.add_node("YES_IMSI_CHANGED",
                      label="Check and confirm with BSS whether SIM has been changed for the user and get UE info updated in VIP Enrichment", shape='box')
        self.add_node("NO_IMSI_NOT_CHANGED",
                      label='IMEI / device Changed for the user', shape="diamond")
        self.add_node("YES_IMEI_CHANGED",
                      label='Get UE info updated in the VIP Enrichment', shape="box")
        self.add_node("NO_IMEI_NOT_CHANGED",
                      label='Check with Radcom for alarm trigger RCA', shape="box")

    def _add_edges(self):
        self.add_edge("START", 'IMSI_CHANGED_ALARM',
                      label='For IMSI / IMEI Change Alarm')
        self.add_edge("IMSI_CHANGED_ALARM", 'IS_IMSI_CHANGED')
        self.add_edge("IS_IMSI_CHANGED", 'YES_IMSI_CHANGED', label='Yes')
        self.add_edge("IS_IMSI_CHANGED", 'NO_IMSI_NOT_CHANGED', label='No')
        self.add_edge("NO_IMSI_NOT_CHANGED", 'YES_IMEI_CHANGED', label='Yes')
        self.add_edge("NO_IMSI_NOT_CHANGED", 'NO_IMEI_NOT_CHANGED', label='No')

    def show_graph(self):
        for n in self.nodes:
            n.update({'physics': False})
        self.show("imsi.html")


if __name__ == '__main__':
    imsi = IMSI()
    imsi.show_graph()
