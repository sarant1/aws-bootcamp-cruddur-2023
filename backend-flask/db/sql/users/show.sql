SELECT
    user.uuid,
    users.handle,
    users.display_name
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    SELECT 
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.created_at,
        activities.expires_at
    FROM public.activities
    WHERE 
        activities.user.uuid = users.uuid
    ORDER BY activities.created_at DESC
    ) array_row) as activities
    LIMIT 40    
FROM public.users
WHERE
    users.id = %(handle)s
