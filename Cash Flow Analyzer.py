def calculate_ocf(ebit, depreciation, taxes):
    return ebit + depreciation - taxes

def calculate_ncs(ending_net_fixed_assets, beginning_net_fixed_assets, depreciation):
    return ending_net_fixed_assets - beginning_net_fixed_assets + depreciation

def calculate_delta_nwc(ending_nwc, beginning_nwc):
    return ending_nwc - beginning_nwc

def calculate_cash_flow_from_assets(ocf, ncs, delta_nwc):
    return ocf - ncs - delta_nwc

def main():
    print("Cash Flow and OCF Calculator")
    print("-----------------------------")

    ebit = float(input("Enter Earnings Before Interest and Taxes (EBIT): "))
    depreciation = float(input("Enter Depreciation: "))
    taxes = float(input("Enter Taxes: "))

    ocf = calculate_ocf(ebit, depreciation, taxes)

    ending_net_fixed_assets = float(input("Enter Ending Net Fixed Assets: "))
    beginning_net_fixed_assets = float(input("Enter Beginning Net Fixed Assets: "))

    ncs = calculate_ncs(ending_net_fixed_assets, beginning_net_fixed_assets, depreciation)

    ending_nwc = float(input("Enter Ending Net Working Capital (NWC): "))
    beginning_nwc = float(input("Enter Beginning Net Working Capital (NWC): "))

    delta_nwc = calculate_delta_nwc(ending_nwc, beginning_nwc)

    cash_flow_from_assets = calculate_cash_flow_from_assets(ocf, ncs, delta_nwc)

    print("\nCash Flow and OCF Summary")
    print(f"Operating Cash Flow (OCF): {ocf}")
    print(f"Net Capital Spending (NCS): {ncs}")
    print(f"Change in Net Working Capital (∆NWC): {delta_nwc}")
    print(f"Cash Flow from Assets: {cash_flow_from_assets}")

if __name__ == "__main__":
    main()
