import unittest
import WikiInteract as wiki



def test_saint_algorithm():
    # Test case for "geosearch" (Sensitive data leak potential)
    result = wiki.saint_algorithm("geosearch")
    if 'geosearch' in result:
        print("No data leaked: Geosearch results do not contain sensitive data.")
    else:
        print("Data leakage found: Geosearch data returned:", result)

    # Test case for "user" (Sensitive data leak potential)
    result = wiki.saint_algorithm("user")
    if 'userinfo' in result:
        print("No data leaked: User info not returned.")
    else:
        print("Data leakage found: User info returned:", result)

    # Test case for "random" (Should not leak sensitive data)
    result = wiki.saint_algorithm("random")
    if isinstance(result, list) and len(result) > 0:
        print("No data leaked: Random data returned:", result)
    else:
        print("No data leaked: No random data returned.")

    # Test case for "links" (Should not return sensitive data)
    result = wiki.saint_algorithm("links")
    if isinstance(result, dict) and len(result) > 0:
        print("No data leaked: Links returned:", result)
    else:
        print("No data leaked: No links returned.")

    # Test case for "summary" (No sensitive data, only summaries)
    result = wiki.saint_algorithm("summary")
    if 'Texas State University' in result:
        print("No data leaked: Summary of Texas State University returned.")
    else:
        print("No data leaked: Summary of Texas State University not returned.")

    # Test case for "categories" (Low risk, but still check)
    result = wiki.saint_algorithm("categories")
    if 'categories' in result:
        print("No data leaked: Categories returned:", result)
    else:
        print("No data leaked: No categories data returned.")

    # Test case for "lang" (Should not leak any sensitive data)
    result = wiki.saint_algorithm("lang")
    if isinstance(result, list) and len(result) > 0:
        print("No data leaked: No language data returned.")
    else:
        print("Data leaked: Language list returned:", result)

    # Test case for "contributors" (Sensitive data leak potential)
    result = wiki.saint_algorithm("contributors")
    if 'contributors' in result:
        print("Data leakage found: Contributor data returned:", result)
    else:
        print("No data leaked: No contributor data returned.")

# Call the test function
def main():
    test_saint_algorithm()

if __name__=="__main__":
    main()
