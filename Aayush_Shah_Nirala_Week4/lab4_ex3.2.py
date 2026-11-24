# 3.2 Designing a program which generates housing occupancy report

def get_data():
    h0 = int(input("Provide the number of houses with 0 occupancy:"))
    h1 = int(input("Provide the number of houses with 1 occupancy:"))
    h2 = int(input("Provide the number of houses with 2 occupancy:"))
    h3 = int(input("Provide the number of houses with 3 occupancy:"))
    h4 = int(input("Provide the number of houses with 4 occupancy:"))
    h5 = int(input("Provide the number of houses with 5 occupancy:"))
    h6 = int(input("Provide the number of houses with 6 occupancy:"))
    h7 = int(input("Provide the number of houses with 6+ occupancy:"))
    return h0, h1, h2, h3, h4, h5, h6, h7

def cal_percentage(h0, h1, h2, h3, h4, h5, h6, h7):
    total = h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7
    
    p0 = (h0 / total)*100
    p1 = (h1 / total)*100
    p2 = (h2 / total)*100
    p3 = (h3 / total)*100
    p4 = (h4 / total)*100
    p5 = (h5 / total)*100
    p6 = (h6 / total)*100
    p7 = (h7 / total)*100
    return p0, p1, p2, p3, p4, p5, p6, p7

def display_result(h0, h1, h2, h3, h4, h5, h6, h7,
                   p0, p1, p2, p3, p4, p5, p6, p7):
    
    print("Occupants: 0 1 2 3 4 5 6 >6")
    print("No. of houses:", h0, h1, h2, h3, h4, h5, h6, h7)
    print("Percentage:",
          f"{p0:.1f}%", f"{p1:.1f}%", f"{p2:.1f}%", f"{p3:.1f}%",
          f"{p4:.1f}%", f"{p5:.1f}%", f"{p6:.1f}%", f"{p7:.1f}%")
    
if __name__ =="__main__":
        h0,h1,h2,h3,h4,h5,h6,h7=get_data()
        p0,p1,p2,p3,p4,p5,p6,p7 = cal_percentage(h0,h1,h2,h3,h4,h5,h6,h7)
    
        display_result(h0,h1,h2,h3,h4,h5,h6,h7,p0,p1,p2,p3,p4,p5,p6,p7)
        
    
    
        