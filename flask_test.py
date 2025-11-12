from pydriller import Repository
from datetime import datetime

repo_url = "https://github.com/django/django.git"

count = 0
target = 20  # number of commits with deleted Python lines

# only look at commits since Jan 1, 2024
# since_date = datetime(2024, 1, 1)


for commit in Repository(repo_url).traverse_commits():
    print(commit.hash)
    for mod in commit.modifications:
        print("  ", mod.filename, "deleted:", mod.deleted_lines)
    break


# for commit in Repository(
#     repo_url,
#     since=since_date,
#     only_modifications_with_file_types=['.py']
# ).traverse_commits():
#     # skip commits with no modifications
#     if not hasattr(commit, "modifications") or not commit.modifications:
#         continue
#
#     # sum deleted Python lines
#     deleted_total = sum(mod.deleted_lines for mod in commit.modifications)
#     if deleted_total == 0:
#         continue  # skip commits with no deleted Python code
#
#     # print commit info
#     print("Hash:", commit.hash)
#     print("Author:", commit.author.name)
#     print("Date:", commit.author_date)
#     print("Message:", commit.msg)
#     print("Files changed:", len(commit.modifications))
#     print("Deleted lines:", deleted_total)
#     print("-" * 20)
#
#     # print actual deleted lines per file
#     for mod in commit.modifications:
#         print(f"File: {mod.filename}")
#         if hasattr(mod, "diff_parsed") and mod.diff_parsed:
#             for change in mod.diff_parsed:
#                 for line in change.get('deleted', []):
#                     print("-", line)
#         print("-" * 20)
#
#     print("=" * 60)
#
#     count += 1
#     if count == target:
#         break
