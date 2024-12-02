from datetime import datetime
import WikiInteract as wiki



def test_saint_algorithm():
    counter = 0
    # Test case for "datetime" (Sensitive data leak potential)
    today = datetime.now()
    result = wiki.saint_algorithm("date")
    if today == result:
        print("No data leaked: Datetime results do not contain sensitive data.")
    else:
        counter = counter + 1
        print("Data leakage found: Datetime data returned:", result)

    # Test case for "geosearch" (Sensitive data leak potential)
    result = wiki.saint_algorithm("geosearch")
    if 'geosearch' in result:
        print("\nNo data leaked: Geosearch results do not contain sensitive data.")
    else:
        counter = counter + 1
        print("\nData leakage found: Geosearch data returned:", result)

    # Test case for "user" (Sensitive data leak potential)
    result = wiki.saint_algorithm("user")
    if 'userinfo' in result:
        print("\nNo data leaked: User info not returned.")
    else:
        counter = counter + 1
        print("\nData leakage found: User info returned:", result)

    # Test case for "page" (Sensitive data leak potential)
    result = wiki.saint_algorithm("page")
    if 'Texas State University' in result:
        print("\nNo data leaked: Page results do not contain sensitive data.")
    else:
        counter = counter + 1
        print("\nData leakage found: Page data returned:", result)

    # Test case for "random" (Should not leak sensitive data)
    result = wiki.saint_algorithm("random")
    if isinstance(result, list) and len(result) > 0:
        print("\nNo data leaked: Random data returned:", result)
    else:
        print("\nNo data leaked: No random data returned.")

    # Test case for "links" (Should not return sensitive data)
    result = wiki.saint_algorithm("links")
    if isinstance(result, dict) and len(result) > 0:
        print("\nNo data leaked: Links returned:", result)
    else:
        print("\nNo data leaked: No links returned.")

    # Test case for "summary" (No sensitive data, only summaries)
    result = wiki.saint_algorithm("summary")
    if 'Texas State University' in result:
        print("\nNo data leaked: Summary of Texas State University returned.")
    else:
        print("\nNo data leaked: Summary of Texas State University not returned.")

    # Test case for "categories" (Low risk, but still check)
    result = wiki.saint_algorithm("categories")
    if 'categories' in result:
        print("\nNo data leaked: Categories returned:", result)
    else:
        print("\nNo data leaked: No categories data returned.")

    # Test case for "lang" (Should not leak any sensitive data)
    result = wiki.saint_algorithm("lang")
    if isinstance(result, list) and len(result) > 0:
        print("\nNo data leaked: No language data returned.")
    else:
        counter = counter + 1
        print("\nData leaked: Language list returned:", result)

    # Test case for "contributors" (Sensitive data leak potential)
    result = wiki.saint_algorithm("contributors")
    if 'contributors' in result:
        counter = counter + 1
        print("\nData leakage found: Contributor data returned:", result)
    else:
        print("\nNo data leaked: No contributor data returned.")

    print(counter, "/10 Potential Leaks found.")

# Call the test function
def main():
    test_saint_algorithm()

if __name__=="__main__":
    main()
