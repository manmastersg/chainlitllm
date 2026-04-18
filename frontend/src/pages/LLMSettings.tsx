import { apiClient } from '@/api';
import {
  Activity,
  CheckCircle2,
  Clock,
  Cpu,
  Layers,
  Settings2,
  ShieldCheck,
  XCircle,
  Zap
} from 'lucide-react';
import { useEffect, useState } from 'react';
import { Navigate } from 'react-router-dom';

import Page from 'pages/Page';

import { useAuth } from '@chainlit/react-client';

import { Badge } from '@/components/ui/badge';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle
} from '@/components/ui/card';
import { Separator } from '@/components/ui/separator';

interface LLMSettingsData {
  provider_id: string;
  provider_type: string;
  api_key: string;
  enable_thinking: boolean;
  enable_streaming: boolean;
  is_active: boolean;
  [key: string]: any;
}

const LLMSettings = () => {
  const { user, isReady } = useAuth();
  const [settings, setSettings] = useState<LLMSettingsData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const role = user?.metadata?.role;

  useEffect(() => {
    if (!isReady || role !== 'admin') return;

    const fetchSettings = async () => {
      const endpoint = '/project/llm-settings';
      console.log(`[LLMSettings] Fetching from: ${endpoint}`);
      try {
        const response = await apiClient.get(endpoint);
        console.log(`[LLMSettings] Response status: ${response.status}`);

        if (!response.ok) {
          const errorText = await response.text();
          console.error(`[LLMSettings] Request failed: ${errorText}`);
          throw new Error(`Failed to fetch LLM settings: ${response.status}`);
        }

        const contentType = response.headers.get('content-type');
        console.log(`[LLMSettings] Content-Type: ${contentType}`);

        const text = await response.text();
        if (!contentType || !contentType.includes('application/json')) {
          console.error(
            `[LLMSettings] Received non-JSON response:`,
            text.substring(0, 200)
          );
          throw new Error(
            'Server returned HTML instead of configuration. Please ensure you are logged in as an admin.'
          );
        }

        const data = JSON.parse(text);
        console.log(`[LLMSettings] Data received:`, data);
        const provider = data.providers?.[0] || data;

        if (!provider) {
          throw new Error('No LLM provider configuration found.');
        }

        setSettings({
          ...provider,
          provider_id: provider.id || 'unknown'
        });
      } catch (err: any) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchSettings();
  }, [role, isReady]);

  // Wait for auth to be ready before making a redirection decision
  if (!isReady) {
    return (
      <Page>
        <div className="flex items-center justify-center py-20">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
        </div>
      </Page>
    );
  }

  if (role !== 'admin') {
    return <Navigate to="/" replace />;
  }

  const SettingRow = ({ icon: Icon, label, value, isBadge = false }: any) => (
    <div className="flex items-center justify-between py-3">
      <div className="flex items-center gap-3">
        <div className="p-2 bg-primary/10 rounded-lg text-primary">
          <Icon size={18} />
        </div>
        <span className="text-sm font-medium text-muted-foreground">
          {label}
        </span>
      </div>
      <div className="flex items-center">
        {isBadge ? (
          <Badge
            variant={value ? 'default' : 'secondary'}
            className="flex gap-1 items-center"
          >
            {value ? <CheckCircle2 size={12} /> : <XCircle size={12} />}
            {value ? 'Enabled' : 'Disabled'}
          </Badge>
        ) : (
          <span className="text-sm font-semibold">{value || 'N/A'}</span>
        )}
      </div>
    </div>
  );

  return (
    <Page>
      <div className="container max-w-4xl py-10 animate-in fade-in duration-500">
        <div className="mb-8">
          <h1 className="text-3xl font-bold tracking-tight text-primary">
            LLM Configuration
          </h1>
          <p className="text-muted-foreground mt-1">
            Manage and monitor your language model provider settings.
          </p>
        </div>

        {loading ? (
          <div className="flex flex-col items-center justify-center py-20 gap-4">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
            <p className="text-muted-foreground animate-pulse">
              Loading settings...
            </p>
          </div>
        ) : error ? (
          <Card className="border-destructive/50 bg-destructive/5">
            <CardHeader>
              <CardTitle className="text-destructive flex items-center gap-2">
                <XCircle size={20} />
                Error Loading Settings
              </CardTitle>
              <CardDescription>{error}</CardDescription>
            </CardHeader>
          </Card>
        ) : (
          settings && (
            <div className="grid gap-6">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-lg">
                  <CardHeader className="pb-2">
                    <CardTitle className="text-sm font-medium text-muted-foreground flex items-center gap-2">
                      <Activity size={16} /> Status
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="flex items-center gap-2">
                      <div
                        className={`h-2.5 w-2.5 rounded-full ${settings.is_active ? 'bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)]' : 'bg-red-500'}`}
                      />
                      <span className="text-2xl font-bold">
                        {settings.is_active ? 'Active' : 'Inactive'}
                      </span>
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-lg">
                  <CardHeader className="pb-2">
                    <CardTitle className="text-sm font-medium text-muted-foreground flex items-center gap-2">
                      <Layers size={16} /> Type
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <span className="text-2xl font-bold uppercase">
                      {settings.provider_type}
                    </span>
                  </CardContent>
                </Card>

                <Card className="bg-card/50 backdrop-blur-sm border-primary/20 shadow-lg">
                  <CardHeader className="pb-2">
                    <CardTitle className="text-sm font-medium text-muted-foreground flex items-center gap-2">
                      <Cpu size={16} /> Provider ID
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <span className="text-2xl font-bold truncate block">
                      {settings.provider_id}
                    </span>
                  </CardContent>
                </Card>
              </div>

              <Card className="bg-card/50 backdrop-blur-sm border-primary/10 shadow-xl overflow-hidden">
                <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-primary/50 via-primary to-primary/50" />
                <CardHeader>
                  <div className="flex items-center gap-2 text-primary mb-1">
                    <Settings2 size={20} />
                    <CardTitle>Core Parameters</CardTitle>
                  </div>
                  <CardDescription>
                    Configuration details for the active LLM provider.
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-1">
                  <SettingRow
                    icon={ShieldCheck}
                    label="API Key Status"
                    value={settings.api_key ? 'Configured' : 'Missing'}
                  />
                  <Separator className="opacity-50" />
                  <SettingRow
                    icon={Zap}
                    label="Streaming"
                    value={settings.enable_streaming}
                    isBadge
                  />
                  <Separator className="opacity-50" />
                  <SettingRow
                    icon={Clock}
                    label="Thinking Mode"
                    value={settings.enable_thinking}
                    isBadge
                  />
                </CardContent>
              </Card>

              <div className="bg-muted/30 rounded-lg p-4 border border-border/50 text-xs text-muted-foreground flex items-center gap-2">
                <CheckCircle2 size={14} className="text-primary" />
                This configuration is currently being used for all model
                interactions in the chat interface.
              </div>
            </div>
          )
        )}
      </div>
    </Page>
  );
};

export default LLMSettings;
