#List of incidents, filtered by status, summary

#1. Create dic of INC

incident = {
    'incident_id' : 'INC-404',
    'category' : 'Balance Spike',
    'amount_impacted' : 240_000_500,
    'currency' : 'USD',
    'source_system' : 'FFS',
    'status' : 'OPEN',
    'assigned to' : 'PK'
}

#Access
print( 'Incident ID:',  incident['incident_id'])

#update
incident['status'] = 'in_progress'
print('Status updated to:', incident['status'])

#Add
incident['root_cause'] = 'feed_delay'
print('Root Cause:' ,incident['root_cause'])

##=====================================================

root_cause = incident.get('root_cause', 'not_identified')
print('The RCA:',root_cause)


resolver = incident.get('resolved_by', 'not_identified')
print("Missing key via .get():", resolver)

if 'root_cause' in incident:
    print("root_cause is present:", incident['root_cause'])
 
if 'resolved_by' not in incident:
    print("resolved_by not yet set — investigation ongoing")
 

 #===================================================
incidents = [{'incident_id' : 'INC-407',
    'category' : 'Balance Spike',
    'amount_impacted' : 850_120_000_500,
    'currency' : 'USD',
    'source_system' : 'GLRS',
    'status' : 'OPEN',
    'assigned to' : 'PK'
    },

    {
    'incident_id' : 'INC-550',
    'category' : 'Toxic combination',
    'amount_impacted' : 123_869,
    'currency' : 'USD',
    'source_system' : 'LRR',
    'status' : 'OPEN',
    'assigned to' : 'VG'
    },

    {
    'incident_id' : 'INC-570750',
    'category' : 'YTM_PCT flowing incorrectly',
    'amount_impacted' : 540_729_786,
    'currency' : 'USD',
    'source_system' : 'LUSRRIRR',
    'status' : 'Closed',
    'assigned to' : 'MG'
    }]
    
 
print("Incident Summary:")
for inc in incidents:
   print(
        f"{inc['incident_id']} | "
        f"{inc['category']} | "
        f"{inc['amount_impacted']:,} | "
        f"{inc['status']}"
    )
 