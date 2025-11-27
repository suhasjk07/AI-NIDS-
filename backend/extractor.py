from scapy.all import rdpcap

def extract_flows_from_pcap(pcap_path):
    try:
        pkts = rdpcap(pcap_path)
    except Exception as e:
        print('Error reading pcap', e)
        return []
    flows = {}
    for p in pkts:
        if not p.haslayer('IP'):
            continue
        ip = p['IP']
        src = ip.src; dst = ip.dst
        proto = ip.proto
        sport = getattr(p, 'sport', 0)
        dport = getattr(p, 'dport', 0)
        key = (src,dst,sport,dport,proto)
        if key not in flows:
            flows[key] = {'src_ip':src,'dst_ip':dst,'src_port':sport,'dst_port':dport,'proto':proto,'packets':0,'bytes':0,'start':None,'end':None}
        flows[key]['packets'] += 1
        flows[key]['bytes'] += len(p)
    out = []
    for k,v in flows.items():
        v['duration'] = 1.0
        out.append(v)
    return out
