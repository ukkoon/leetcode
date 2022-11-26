from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            fields = email.split("@")
            local_name = fields[0]
            domain_name = fields[1]
            
            if '+' in local_name:
                local_name = local_name[0:local_name.find('+')]
            
            result.add(f"{local_name.replace('.','')}@{domain_name}")
        
        return len(result)