# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d 
# (with space in between), inclusively. In other words, we should 
# include elements s[b] and s[d]in our slice.

{
    s = "E54aE7M1xoW72UU6hpsDXwN8GAf91csliIKljswvhTRFrmA6ElX8EvswxfWrhZu6XinDznO1FCX1n94FMiddendorffinaiaHAdwOHkji9p0QPtQWaMJFLRZV3z2lritGPCVM677s4S8NsG6teSjGdderemensisdX4rMUSaenGAu42azfbCVA05B8LdG."
    a, b, c, d = 80, 95, 150, 159
    slice1=s[a:b+1]
    slice2=s[c:d+1]
    slice1 +" " + slice2
}

# 'Middendorffinaia deremensis'